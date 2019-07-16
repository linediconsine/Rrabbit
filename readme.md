# Random Rabbit
Using, Python - Flask - React

Randomic Rabbit is a web service that generates random numbers at random time intervals, and sends them to the connected user in real time.

No memory about generated numbers is maintained.

Given:

- A server that generates random numbers at random time intervals
- Sends them to the connected user in real time. 
- No memory about generated numbers is maintained.


The closest thing I know that I use for this is a _messaging broker_. So I thought to give him a shoot.

I used [RabbitMQ](https://www.rabbitmq.com) in the simplest configuration that I found [here](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

After this, the missing part is create a web interface that dynamically show the keys.

## Requirements
1. Install RabbitMQ and run RabbitMQ server
2. Python3
3. For install all python libraries needed please use:
$ pip install -r requirements.txt

## How to run

1- run rabbitMQ server  

Run is the message broeker 

2- run randomRabbitServer/RandomRabbit_server.py 

Run the token generator, I will send message to any User connected to the same queue 

3- run rabbitUser/RandomRabbit_receiver.py

Run the RandomRabbit receiver that provide two way to ispect what he has received:
1) /html
2) /json

4- on rabbitUser/webapp run: npm start

A more dyanamic wait to visulize Received data, in a Comodore64 style UI...well, kind of...


## What is missing...
Also know as __"Opsy, I finished the time"__

1. RabbitMQ confguration: It works out of the box

2. Test: Shame on me, I should have make at least a couple of unit test

2. Makefile ( and easy start stop whould be great)

3. gitignore ... ... 
