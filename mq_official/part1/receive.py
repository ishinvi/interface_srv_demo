#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : receive.py
# @Author: 蒋光谱
# @Date  : 2019/3/22
# @Desc  :
from datetime import datetime

import pika

# 建立和队列服务器的连接，如果连接到不同机器上，要指定IP

credentials=pika.PlainCredentials('admin','a544460159')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',
                                                               port='5672',
                                                               virtual_host='/',
                                                               credentials=credentials))
channel = connection.channel()

# 在接收前，先确定队列是否存在，不存在则创建
channel.queue_declare(queue='hello')


# 通过回调来处理消息
def callback(ch, method, properties, body):
    print('[x] Received %r %s' % (body,datetime.now()))


# 告诉mq在hello队列收到消息时，调用callback
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

# 等待消息
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
