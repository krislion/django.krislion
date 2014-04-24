from django import http
from google.appengine.api import mail
import cgi
import django.core.context_processors
from django.core.context_processors import csrf

def home(request):
    DEFAULT_PAGE='''
<html>
<head><title>Kris Lion</title>
<style type="text/css">
body {background-color:#ffffff;color:#ffffff;font-family:Arial, Verdana, sans-serif;margin:0px 0px 0px 0px;font-size:1.1em;}
.right-side-effect {background-image:-moz-linear-gradient(center right,#feffff,#4577cb);
background-image:-ms-linear-gradient(right,#4577cb,#3264b6);
background-image:-webkit-gradient(linear,0 0,100% 0,from(#4577cb),to(#feffff));
background-image:-webkit-linear-gradient(right,#feffff,#4577cb);
background-image:-o-linear-gradient(right,#feffff,#4577cb);
background-image:linear-gradient(right,#feffff,#4577cb);
background-repeat:y;}
.div2 {background-color:#ccefe9;border-radius:50px;margin:20px 50px;padding:20px;}
.content-all {background-color:#ffffff;min-width:235px;max-width:1920px;display:block;}
.nav-main {background-color:#3d6fc3;padding:15px 0px 15px 0px;
background-image:-moz-linear-gradient(center top,#4577cb,#3264b6);
background-image:-ms-linear-gradient(top,#4577cb,#3264b6);
background-image:-webkit-gradient(linear,0 0,0 100%,from(#4577cb),to(#3264b6));
background-image:-webkit-linear-gradient(top,#4577cb,#3264b6);
background-image:-o-linear-gradient(top,#4577cb,#3264b6);
background-image:linear-gradient(top,#4577cb,#3264b6);
background-repeat:x;}
.content-main {background-color:#009fe9;padding:10px 0px 10px 0px;text-align:center;}
.right-hand-filler {background-color:#ffffff;width:30px;display:block;}
.logo-main {margin:0px 0px 0px 20px;padding:10px 0px 10px 20px;font-size:200%}
.logo-main a{text-decoration:none;}
.logo-main a:visited{color:#ffffff;}
.logo-main a:visited:hover{color:#bbff11;}
.logo-subtitle {padding:10px 0px 20px 10px;font-size:50%;vertical-align:middle;margin-top:15px;}
.cart {padding: 0 20px 0 0;vertical-align:middle;float:right;}
.header-linkedin{padding 0 0 0 0;margin-right:30px;vertical-align:middle;float:right;background-color:#007fd2;
border-radius: 8px;
-moz-border-radius: 8px;
-webkit-border-radius: 8px;
transition: background 0.5s ease-in-out;}
.header-facebook, .header-twitter, .header-github, .header-deviantart, .header-googleplus, .header-steam{padding 0 0 0 0;margin-right:10px;vertical-align:middle;float:right;background-color:#007fc9;
border-radius: 8px;
-moz-border-radius: 8px;
-webkit-border-radius: 8px;
transition: background 0.5s ease-in-out;}
.header-facebook:hover, .header-linkedin:hover, .header-twitter:hover, .header-github:hover, .header-deviantart:hover, .header-googleplus:hover, .header-steam:hover{fill:#bbff11;background-color:#22aff4;}
.author-attribution {font-style:normal;font-size:75%;padding-left:10px;float:right;}
.content-fun {background-image:url("images/catch-drone-zoom-1920-2.jpg");height:690px;background-repeat:no-repeat;background-position:left top;}
@media (max-width:1660px) {
 .content-fun {background-image:url("images/catch-drone-zoom-1680-2.jpg");}
}
@media (max-width:1020px) {
 .content-fun {background-image:url("images/catch-drone-zoom-1024.jpg");height:425px;}
}
@media (max-width:840px) {
 .logo-subtitle {display:none;}
}
@media (max-width:610px) {
 .header-googleplus {display:none;}
}
@media (max-width:550px) {
 .header-deviantart {display:none;}
}
@media (max-width:490px) {
 .header-github {display:none;}
}
@media (max-width:430px) {
 .header-twitter {display:none;}
}
@media (max-width:370px) {
 .header-steam {display:none;}
}
@media (max-width:310px) {
 .header-facebook {display:none;}
}
@media (max-width:640px) {
 .logo-main {padding:10px 0 10px 5px;}
 .header-linkedin{margin-right:10px;}
}
@media (max-height:650px) {
 .content-fun{height:425px}
}
.footer {text-align:center;padding:20px 0px 30px 15px;margin-bottom:0px;
background-image:-moz-linear-gradient(center top,#009fe9,#3284d6);
background-image:-ms-linear-gradient(top,#009fe9,#3264b6);
background-image:-webkit-gradient(linear,0 0,0 100%,from(#009fe9),to(#3264b6));
background-image:-webkit-linear-gradient(top,#009fe9,#3264b6);
background-image:-o-linear-gradient(top,#009fe9,#3264b6);
background-image:linear-gradient(top,#009fe9,#3264b6);
background-repeat:x;}
.follow-me {padding-left:25px;}
.copyright {vertical-align:middle;font-size:1em}
.li-btn {vertical-align:middle;}
a:visited {color:#ddff66;
transition:color 0.18s ease;}
a:link {color:#ffffff;
transition:color 0.18s ease;}
a:hover {color:#bbff11;}
a:active {color:#44ff11;}
</style></head>
<body>
 <div class="content-all">
  <div class="nav-main">
   <span class="logo-main"><a href="#">Kris Lion
   <span class="logo-subtitle">"Power to the People!"</span></a></span>
   <!--<span class="logo-subtitle">"Passion: refer to Kristopher Lion."</span>-->
   <!--<span class="cart"><a href="http://linkedin.krislion.com"><img src="images/cart.svg" height="50px" width="50px" /></a></span>-->
   <!--<span class="logo-subtitle">"Ship it!"</span>-->
   <span class="header-linkedin"><a href="http://LINKEDIN.KrisLion.com"><img height="50px" width="50px" src="images/in.svg" /></a></span>
   <span class="header-facebook"><a href="http://FACEBOOK.KrisLion.com"><img height="50px" width="50px" src="images/f.svg" /></a></span>
   <span class="header-twitter"><a href="http://TWITTER.KrisLion.com"><img height="50px" width="50px" src="images/twitter.svg" /></a></span>
   <span class="header-github"><a href="http://GITHUB.KrisLion.com"><img height="50px" width="50px" src="images/github.svg" /></a></span>
   <span class="header-deviantart"><a href="http://DEVIANT.KrisLion.com"><img height="50px" width="50px" src="images/deviantart.svg" /></a></span>
   <span class="header-googleplus"><a href="http://GOOGLEPLUS.KrisLion.com"><img height="50px" width="50px" src="images/gplus.svg" /></a></span>
   <span class="header-steam"><a href="http://STEAM.KrisLion.com"><img height="50px" width="50px" src="images/steam.svg" /></a></span>
  </div>
  <div class="content-fun"><!--<span>Lorem</span><span>Ipsum</span><span>Dolor</span>--></div>
  <!--<div class="second-picture"><!-- no content ></div>-->
  <div class="content-main">
   <a href="http://12THMAN.KrisLion.com">12thMan</a> |
   <a href="http://BOOK.KrisLion.com">Book</a> |
   <!--<a href="http://BROWNALE.KrisLion.com">Brown Ale</a> |-->
   <a href="http://CANADA.KrisLion.com">Canada</a> |
   <a href="http://CONCEPT.KrisLion.com">Concept</a> |
   <a href="http://DRONES.KrisLion.com">Drones</a> |
   <a href="http://MUSIC.KrisLion.com">Music</a> | 
   <a href="http://PONIES.KrisLion.com">Ponies[@1:14-1:22]</a> |
   <a href="http://ZESTAWIT.KrisLion.com">Zestawit</a>
  <div class="content-main">
   <!--<a href="http://kris-lion.blogspot.com/">Blogspot</a> | -->
   <a href="http://DEVIANT.KrisLion.com">DeviantArt</a> | 
   <a href="http://FACEBOOK.KrisLion.com">Facebook</a> | 
   <a href="http://GITHUB.KrisLion.com">Github</a> | 
   <a href="http://GOOGLEPLUS.KrisLion.com">GooglePlus</a> | 
   <!--<a href="http://KRISLION.KrisLion.com">Kris Lion</a> | --> 
   <a href="http://LINKEDIN.KrisLion.com">LinkedIn</a> | 
   <!--<a href="http://MYSPACE.KrisLion.com">MySpace</a> | -->
   <!--<a href="http://PROFILE.KrisLion.com">Profile</a> | --> 
   <a href="http://STEAM.KrisLion.com">Steam</a> | 
   <a href="http://TWITTER.KrisLion.com">Twitter</a> 
  </div>
  <div class="content-main">
    may also contact via [my name]@gmail.com --- kris.lion
    <!--<img height="20px" width="300px" src="images/email.svg" />-->
  </div>
  <!--
   <a href="http://DAVERYACK.KrisLion.com">Dave Ryack</a> |
   <a href="http://KAWASAKI.KrisLion.com">Kawasaki</a> | 
   <a href="http://MARA.KrisLion.com">Mara</a> | 
   <a href="http://MULLINS.KrisLion.com">Mullins</a> | 
   <a href="http://NICK.KrisLion.com">Nick</a> | 
   <a href="http://RANDY.KrisLion.com">Randy</a> | 
   <a href="http://TAYLOR.KrisLion.com">Taylor</a> | 
   <a href="http://TOM.KrisLion.com">Tom</a> | 
   <a href="http://YUSUKE.KrisLion.com">Yusuke</a> | 
  -->
  <div class="footer">
   <span class="copyright">
    <a href="http://LINKEDIN.krislion.com" style="text-decoration:none;">&copy; 2000-2014 Kris Lion
     <span class="li-btn">
      <img src="/images/btn_in_20x15.png" width="20" height="15" alt="View Kris Lion's LinkedIn profile" style="vertical-align:middle;margin-bottom:5px" border="0" />
     </span>
    </a>
   </span>
  </div>
  <!--<div class="right-hand-filler">timetimetime&nbsp;</div>-->
 </div>
 <div class="content-main" style="text-align:left">
  (2014-04-23) Coming soon! (eta 4-25, 28, 30 --- will have updates M-W-F)<br />
  1. chat on page -or- link to online IRC chat client [mibbit]<br />
  2. contact form<br />
  3. favicon.ico - DONE! 2014-04-22<br />
  3. twitter button - DONE! 2014-04-21<br />
  4. steam button - DONE! 2014-04-21<br />
  5. deviantart button - DONE! 2014-04-23<br />
  6. googleplus button - DONE! 2014-04-23<br />
  7. more images<br />
  8. linked sites updates<br />
  9. consider eggplant
 </div>

<form action="/contact" method="post" style="display:none;">
 <div><textarea name="content" rows="3" cols="60"></textarea></div>
 <div><input type="submit" value="SEND CONTACT"></div>
 <div style="display:none">
  <input type="hidden" name="csrfmiddlewaretoken" value="''' + unicode(django.core.context_processors.csrf(request)['csrf_token']) + '''"/>
 </div>
</form>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-50214237-1', 'krislion.com');
  ga('require', 'displayfeatures');
  ga('require', 'linkid', 'linkid.js');
  ga('send', 'pageview');
</script>
</body></html>
'''
    return http.HttpResponse(DEFAULT_PAGE) #('Hello Kris Lion!')


def contact(request):
    retval = '<html><body>You wrote:<pre>'
    retval += unicode(request.POST['content']) #cgi.escape(unicode(request.get('content'))
    retval += '</pre></body></html>'
    message = mail.EmailMessage(sender="kris.lion@gmail.com",subject="Someone is trying to contact me!",to="kris.lion@gmail.com")
    message.body = unicode(request.POST['content'])
    message.send()
    return http.HttpResponse(retval)


from random import choice
from django.utils import simplejson
from google.appengine.api import channel, memcache, users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from django.views.generic import View
from django.shortcuts import redirect, render, render_to_response
ANONYMOUS_IDS = set(range(1, 1000)) # you can increase it for accepting more anonymous users

def broadcast(message, tokens=None):
    if not tokens:
        tokens = memcache.get('tokens')
    if tokens:
        tokens.pop('_used_ids', None) # make sure you won't use the tokens after broadcast(), otherwise you need do a copy
        ids = set(tokens.values()) # remove duplicate ids
        # be noticed that a logged in user may connect to 1 channel by using several browsers at the same time
        # it works strange both in the cloud and local server:
        #   1. if removed the duplicate ids, only the last connected browser can receive the message
        #   2. if not removed them, all the browsers will receive duplicate messages
        # I don't know if it's a bug of the SDK 1.4.0
        for id in ids: # it may take a while if there are many users in the room, I think you can use task queue to handle this problem
            if isinstance(id, int):
                id = 'anonymous(%s)' % id
            channel.send_message(id, message)

class ChatHandler(View):
    def get(self, request, *args, **kwargs):
        return render_to_response("chat.html", {'csrfmiddlewaretoken_token':unicode(csrf(request)['csrf_token'])})

class GetTokenHandler(View):
    def get(self, request, *args, **kwargs):
        tokens = memcache.get('tokens') or {}
        user = users.get_current_user()
        if user:
            channel_id = id = user.email() # you can use hash algorithm for ensuring the channel id is less then 64 bytes
        else:
            used_ids = tokens.get('_used_ids') or set()
            available_ids = ANONYMOUS_IDS - used_ids
            if available_ids:
                available_ids = list(available_ids)
            else:
                return http.HttpResponse('')#elf.response.out.write('')
            id = choice(available_ids)
            used_ids.add(id)
            tokens['_used_ids'] = used_ids
            channel_id = 'anonymous(%s)' % id
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
                    user_name = 'anonymous(%s)' % id
                else:
                    user_name = id.split('@')[0]
                del tokens[token]
                memcache.set('tokens', tokens)
                message = user_name + ' has left the chat room.'
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
                    user_name = 'anonymous(%s)' % id
                else:
                    user_name = id.split('@')[0]
                message = user_name + u' has joined the chat room.'
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
                    user_name = 'anonymous(%s)' % id
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




