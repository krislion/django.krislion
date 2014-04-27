import cgi
import django.core.context_processors
from django import http
from google.appengine.api import mail
from django.core.context_processors import csrf
from random import choice
from django.utils import simplejson
from google.appengine.api import channel, memcache, users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from django.views.generic import View
from django.shortcuts import redirect, render, render_to_response


def _get_csrf_token_dict(request):
    return {'csrfmiddlewaretoken_token':unicode(csrf(request)['csrf_token'])} 


def home(request):
    return render_to_response('base.html', _get_csrf_token_dict(request))


def contact(request):
    retval = '<html><body>You wrote:<pre>'
    retval += unicode(request.POST['content'])
    retval += '</pre></body></html>'
    message = mail.EmailMessage(sender="kris.lion@gmail.com",subject="Someone is trying to contact me!",to="kris.lion@gmail.com")
    message.body = unicode(request.POST['content'])
    message.send()
    return http.HttpResponse(retval)


ANONYMOUS_IDS = set(range(1, 100)) #limit on anonymous users
def broadcast(message, tokens=None):
    if not tokens:
        tokens = memcache.get('tokens')
    if tokens:
        tokens.pop('_used_ids', None) #do not use token after broadcast
        ids = set(tokens.values())
        # google-authenticated/logged in user may connect to the same channel using several browsers at a time
        # if we remove duplicates (by using set above), then the last connected browser will receive messages
        # if we leave duplicates, all browsers receive duplicate messages
        for id in ids: # it may take a while if there are many users in the room, I think you can use task queue to handle this problem
            if isinstance(id, int):
                id = 'krislion-fan(%s)' % id
            channel.send_message(id, message)

class ChatHandler(View):
    def get(self, request, *args, **kwargs):
        return render_to_response("chat.html", _get_csrf_token_dict(request))

class GetTokenHandler(View):
    def get(self, request, *args, **kwargs):
        tokens = memcache.get('tokens') or {}
        user = users.get_current_user()
        if user:
            channel_id = id = user.email() # consider hash to keep id less then 64 bytes
        else:
            used_ids = tokens.get('_used_ids') or set()
            available_ids = ANONYMOUS_IDS - used_ids
            if available_ids:
                available_ids = list(available_ids)
            else:
                return http.HttpResponse('')
            id = choice(available_ids)
            used_ids.add(id)
            tokens['_used_ids'] = used_ids
            channel_id = 'krislion-fan(%s)' % id
        token = channel.create_channel(channel_id)
        tokens[token] = id
        memcache.set('tokens', tokens) # you can use datastore instead of memcache
        return http.HttpResponse(token)

class ReleaseTokenHandler(View):
    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        if not token:
            return
        tokens = memcache.get('tokens')
        if tokens:
            id = tokens.get(token, '')
            if id:
                if isinstance(id, int):
                    used_ids = tokens.get('_used_ids')
                    if used_ids:
                        used_ids.discard(id)
                        tokens['_used_ids'] = used_ids
                    user_name = 'krislion-fan(%s)' % id
                else:
                    user_name = id.split('@')[0]
                del tokens[token]
                memcache.set('tokens', tokens)
                message = user_name + ' left the chat.'
                message = simplejson.dumps(message)
                broadcast(message, tokens)
        return django.http.HttpResponse("")

class OpenHandler(View):
    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        if not token:
            return
        tokens = memcache.get('tokens')
        if tokens:
            id = tokens.get(token, '')
            if id:
                if isinstance(id, int):
                    user_name = 'krislion-fan(%s)' % id
                else:
                    user_name = id.split('@')[0]
                message = user_name + u' joined the chat.'
                message = simplejson.dumps(message)
                broadcast(message, tokens)
        return django.http.HttpResponse("")

class ReceiveHandler(View):
    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        if not token:
            return
        message = request.POST.get('content')
        if not message:
            return
        tokens = memcache.get('tokens')
        if tokens:
            id = tokens.get(token, '')
            if id:
                if isinstance(id, int):
                    user_name = 'krislion-fan(%s)' % id
                else:
                    user_name = id.split('@')[0]
                message = '%s: %s' % (user_name, message)
                message = simplejson.dumps(message)
                if len(message) > channel.MAXIMUM_MESSAGE_LENGTH:
                    return
                broadcast(message)
        return django.http.HttpResponse("")

class LoginOrOut(View):
    def get(self, request, *args, **kwargs):
        if users.get_current_user():
            return redirect(users.create_logout_url('/chat'))
        else:
            return redirect(users.create_login_url('/chat'))


