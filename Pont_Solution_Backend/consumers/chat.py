import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.apps import apps
from channels.db import database_sync_to_async
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "chat"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
      
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def create_message(self, message):
       
        Message = apps.get_model('app_messages', 'Message')
       
        msg = Message.objects.create(message=message)

        return msg.timestamp.strftime('%H:%M')  
    


    async def receive(self, text_data):

        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        
        timestamp = await self.create_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'time': timestamp,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        time = event['time']

        await self.send(text_data=json.dumps({
            'message': message,
            'time': time,
        }))
