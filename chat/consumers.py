from django.http import HttpResponse
from channels.handler import AsgiHandler
import json

from channels.channel import Group

def ws_connect(message):
    Group('chat').add(message.reply_channel)

def ws_message(message):
    try:
       data = json.loads(message['text'])
    except ValueError:
       print("ws message isn't json text=%s", message['text'])
       return
    Group('chat').send({'text': json.dumps({'message': data,
                                            'sender': message.reply_channel.name})}),

def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)