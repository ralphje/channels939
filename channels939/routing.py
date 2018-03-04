from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from example.consumers import StuffConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        url("^stuff/$", StuffConsumer),
    ])
})
