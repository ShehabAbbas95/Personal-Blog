import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import *
from django.core import serializers
import channels.layers
class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
        "type": "websocket.accept"

        })
        # other_user = self.scope['url_route']['kwargs']['username']
        # me = self.scope['user']
        # print(other_user, me)
        # threads = await self.get_thread(me,other_user)
        # print(thread)
        chat_room = 'X'
        self.chat_room = chat_room
        await self.channel_layer.group_add(
        chat_room ,
        self.channel_name
        )
    async def websocket_receive(self, event):
        print('receieved', event)
        # username = 'default'
        # user = self.scope['user']
        # if user.is_authenticated:
        #     username = user.username
        msg_info= event.get('text',None)
        data =json.loads(msg_info)
        print(data["comment"],data["username"],data["post_id"])
        save = await self.saving_comment(data["comment"],data["username"],data["post_id"])
        # print(data["message"],data["username"])
        # info = {
        # 'message': data["message"],
        # 'username' : data["username"] }
        #
        # print(data["message"],data["username"],data)

        await self.channel_layer.group_send(
        self.chat_room,
        {
            'type':'chat_message',
            "text": msg_info
        }
        )
    async def chat_message(self,event):
        await self.send({
        'type':'websocket.send',
        'text':event['text']
        })
    async def websocket_disconnect(self, event):
        print('disconnected', event)
    @database_sync_to_async
    def saving_comment(self,comment,username,post_id):
        user_data = Userscomment(comment = comment,
        username = username, post_id = post_id)
        user_data.save()
    # @database_sync_to_async
    # def get_thread(self, user,other_username):
    #     return Thread.objects.get_or_new(user,other_username)[0]
