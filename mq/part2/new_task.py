#!/usr/bin/env python

import pika
import sys

# 连接队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# 创建队列，有就不管，没有就自动创建
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"
# 使用默认的交换机发送消息。exchange为空就使用默认的
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print("[x] Sent %r" % message)

connection.close()
