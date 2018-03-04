from channels.generic.websocket import AsyncJsonWebsocketConsumer


class StuffConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("stuff", self.channel_name)
        await self.channel_layer.group_add("stuff2", self.channel_name)
        await self.channel_layer.group_add("stuff3", self.channel_name)
        await self.send_json({"content": "hello, welcome!"})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("stuff", self.channel_name)
        await self.channel_layer.group_discard("stuff2", self.channel_name)

    async def stuff_new_stuff(self, event):
        await self.send_json({"content": event['text']})
