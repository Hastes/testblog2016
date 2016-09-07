import asyncio
@asyncio.coroutine
def client_handler(websocket, uri):
    # Send a message
    yield from websocket.send('Hello world')
    # Read all messages while the socket is open
    while True:
        msg = yield from websocket.recv()
        if msg is None:
            # Oops, the socket has closed
            return
        # Fancy message processing
        print('got message:', msg)
