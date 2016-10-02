from django.http import HttpResponse
from channels.handler import AsgiHandler
import json

from channels.channel import Group

INIT = 0
UPDATE = 1


def ws_connect(message):
    # message.reply_channel.send(json.dumps({
    #     'id': message.reply_channel.name,
    #     "type": INIT
    # }))
    Group('painters').add(message.reply_channel)



def ws_message(message):
    try:
        data = json.loads(message['text'])
    except ValueError:
        print("ws message isn't json text=%s", message['text'])
        return
    Group('painters').send({
        'text': json.dumps({
            'message': data,
            'sender': message.reply_channel.name,
    })}),


def ws_disconnect(message):
    Group('painters').discard(message.reply_channel)