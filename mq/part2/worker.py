#!/usr/bin/env python
import time

import pika

# 连接服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# rabbitmq消费端仍使用此方法创建队列。这样做的意思是：若是没有就创建。和发送端一样。目的是为了保证队列一定会有
channel.queue_declare(queue='hello')


# 收到消息和的回调
def callback(ch, method, properties, body):
    print('[x] Received %r' % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming();
