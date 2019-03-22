#!/usr/bin/env python

import pika

#连接队列服务器
credentials=pika.PlainCredentials('admin','!StrongCX12369874')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='47.105.126.40',
                                                               port='5673',
                                                               virtual_host='/',
                                                               credentials=credentials))

channel=connection.channel()

#创建队列，有就不管，没有就自动创建
channel.queue_declare(queue='hello')

#使用默认的交换机发送消息。exchange为空就使用默认的
for i in range(100):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World! %s' % str(i))

print("[x] Sent 'Hello World'")

connection.close()