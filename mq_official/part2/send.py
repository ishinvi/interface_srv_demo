#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : send.py
# @Author: 蒋光谱
# @Date  : 2019/3/22
# @Desc  :第一章

import pika
import sys

# 建立和队列服务器的连接，如果连接到不同机器上，要指定IP
credentials = pika.PlainCredentials('admin', 'a544460159')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',
                                                               port='5672',
                                                               virtual_host='/',
                                                               credentials=credentials))
channel = connection.channel()

# 在发送前，先确定队列是否存在，不存在则创建
channel.queue_declare(queue='hello', durable=True)  # 队列持久化

# 在 routing_key 中指定列队名称,发送到队列
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 消息持久化，但是这种持久化可靠性不是非常强，如果需要可靠性强的，用publisher confirms
                      ))
print("[x]发送 %r" % message)

connection.close()
