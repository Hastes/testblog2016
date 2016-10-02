import os
import channels.asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stereamtest.settings')

channel_layer = channels.asgi.get_channel_layer()

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(channel_layer)