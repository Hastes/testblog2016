import pusher

pusher_client = pusher.Pusher(
  app_id='242595',
  key='d1b7006b96f7a3a7ffc6',
  secret='d05557adf86d3bd420ec',
  ssl=True
)

#pusher_client.trigger('test_channel', 'my_event', {'message': 'hello world'})