#!/usr/bin/env python
import pika, random, time

def send(key):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='randomic_rabbit_queue')
	channel.basic_publish(exchange='',routing_key='randomic_rabbit_queue', body=key)
	connection.close()


def genrate_json_token(key_lenght = 5):
	new_key = int(random.random() * (10 * 5))
	#timestamp = f"{int(time.time())}-ts--{int(random.random() * (10))}-r"
	#token = {
	#		'timestamp': timestamp,
	#		'key': new_key}
	return new_key


token_generated = 0

if __name__ == "__main__":
	while True:
		token_generated = token_generated +1
		new_token = genrate_json_token()
		waiting_time = int(random.random() * 10)
		send(str(new_token))
		print(f" [{token_generated}] - RandomRabbit will wait {waiting_time} sec and the update the code" , end='\r')
		time.sleep(waiting_time)


