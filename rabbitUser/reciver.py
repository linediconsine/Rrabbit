#!/usr/bin/env python
import threading
from flask import Flask, render_template
import pika



app = Flask(__name__)

# RabbitMQ configuration
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='randomic_rabbit_queue')

memory = []

def random_rabbit_receiver():
	def callback(ch, method, properties, body):
		memory.append(str(body))
	channel.basic_consume(queue='randomic_rabbit_queue', on_message_callback=callback, auto_ack=True)
	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

@app.route('/')
def view():
	return render_template('./user.html', messages=memory)


if __name__ == '__main__':
	th_token_generator = threading.Thread(target=random_rabbit_receiver, args=())
	th_token_generator.start()
	app.run()
