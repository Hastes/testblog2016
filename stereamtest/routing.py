from channels.routing import route
from chat.consumers import ws_connect, ws_message, ws_disconnect

channel_routing = [
    #route("http.request", "chat.consumers.http_consumer"), добавляется автоматически, если не указано
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]