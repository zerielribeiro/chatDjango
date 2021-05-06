import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['nome_sala']
        self.room_group_name = f'chat_{self.room_name}'

        # entrar na sala

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):

        # sair da sala

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )
    # recebe mesagem

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['message']

    # envia mensagem para sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': mensagem
            }
        )
        # recebe a mesnagem da sala

    async def chat_message(self, event):
        mensagem = event['message']

# envia para websocket
        await self.send(text_data=json.dumps({
                'mensagem': mensagem
            }))
