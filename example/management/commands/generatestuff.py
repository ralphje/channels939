import datetime
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates stuff for the websocket'

    def handle(self, *args, **options):
        channel_layer = get_channel_layer()
        while True:
            async_to_sync(channel_layer.group_send)("stuff", {"type": "stuff.new_stuff",
                                                              "text": "It is now %s" % datetime.datetime.now()})
            async_to_sync(channel_layer.group_send)("stuff2", {"type": "stuff.new_stuff",
                                                               "text": "It is now %s (2)" % datetime.datetime.now()})
            async_to_sync(channel_layer.group_send)("stuff3", {"type": "stuff.new_stuff",
                                                               "text": "It is now %s (3)" % datetime.datetime.now()})
            time.sleep(0.1)
