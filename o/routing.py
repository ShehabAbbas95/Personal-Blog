from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from blog.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket':AllowedHostsOriginValidator(
     AuthMiddlewareStack(
     URLRouter(
     [
        # (?P<post>[\w.@+-]+)
        url(r"^blog/", ChatConsumer),
     ]
     )
     )
    )
})
