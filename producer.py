from kombu.connection import Connection
from kombu import Producer
from time import sleep
from config import settings
data = settings()
connection,exchange,task_queue1,task_queue2,task_queue3 = data.get_settings()
publisher = Producer(connection,exchange=exchange)

#publisher.publish("dta22")
for i in range(100000):
	if i%2==0:
		publisher.publish(str(i),routing_key=task_queue1.routing_key)
		print("Towards Consumer 1 with data as %d"%i)
	elif i%3==0:
		publisher.publish(str(i),routing_key=task_queue2.routing_key)
		print("Towards Consumer 2 with data as %d"%i)
	else:
		publisher.publish(str(i),routing_key=task_queue3.routing_key)
		print("Towards Consumer 3 with data as %d"%i)
	sleep(.1)
publisher.close()
connection.close()
