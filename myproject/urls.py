from django.conf.urls import patterns, include, url
from hello.views import ChatHandler, ReceiveHandler, GetTokenHandler, ReleaseTokenHandler, OpenHandler, LoginOrOut

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
    url(r'^chat$', ChatHandler.as_view()),
    url(r'^contact$', 'hello.views.contact'),
    url(r'^post_msg$', ReceiveHandler.as_view()),
    url(r'^get_token$', GetTokenHandler.as_view()),
    url(r'^del_token$', ReleaseTokenHandler.as_view()),
    url(r'^open$', OpenHandler.as_view()),
    url(r'^login$', LoginOrOut.as_view())
)

