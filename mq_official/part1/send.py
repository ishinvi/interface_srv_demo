#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : send.py
# @Author: 蒋光谱
# @Date  : 2019/3/22
# @Desc  :第一章

import pika

# 建立和队列服务器的连接，如果连接到不同机器上，要指定IP
credentials=pika.PlainCredentials('admin','a544460159')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',
                                                               port='5672',
                                                               virtual_host='/',
                                                               credentials=credentials))
channel = connection.channel()

# 在发送前，先确定队列是否存在，不存在则创建
channel.queue_declare(queue='hello')

# 在 routing_key 中指定列队名称,发送到队列
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello world!')
print("[x]发送'Hello world!'")

connection.close()
