# Message Broker - using RabbitMQ

Here is useful detailt:
If don't know about AMQP, [watch this](https://www.youtube.com/watch?v=XjuiZM7JzPw) basic video
 * config.py - configuration file, contain information regarding Exchange, Queues, and connections to RabbitMQ message broker
 * producer.py - generate data 
 * Consumer#.py - Different consumer

File Description:
* congif.py - RabitMQ congiguration  along with exchange and queue information and setting
* producer.py - that will generate the data
* consumer*.py - that will going to process the data

 
> **Note:**
> - Any consumer can run on multiple nodes at a time, messages will be divided equall in to different consumer i.e if different consumers are running on the same queue, then the messages divided according to the number of the consumers.


How to run:
1. Donload celery and give path to rabitmq DB
2. Run the consumers  
3. Run the producer and enjoy the show
