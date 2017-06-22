from kombu.connection import Connection
from kombu import Producer
from time import sleep
from config import settings
data = settings()
connection,exchange,task_queue1,task_queue2 = data.get_settings()
publisher = Producer(connection,exchange=exchange)

#publisher.publish("dta22")
for i in range(100000):
	if i%2==0:
		publisher.publish(str(i),routing_key=task_queue1.routing_key)
		print(i)
	else:
		publisher.publish(str(i),routing_key=task_queue2.routing_key)
		print(i)
	sleep(.1)
publisher.close()
connection.close()