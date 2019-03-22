#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : test_task.py
# @Author: 蒋光谱
# @Date  : 2019/3/22
# @Desc  :
import asyncio
import threading
import time
import os
import sched
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime

import requests

schedule = sched.scheduler(time.time, time.sleep)


class ServiceRun():
    counter = 0

    @classmethod
    def perform_command(cls, inc):
        try:
            cls.counter += 1

            print('任务%s开始时间%s' % (cls.counter, datetime.now()))
            with ThreadPoolExecutor(100) as executor:
                for i in range(3):
                    executor.submit(cls.job1)
            print('任务%s结束时间%s' % (cls.counter, datetime.now()))

            schedule.enter(inc, 0, cls.perform_command, argument=(inc,))
        except Exception as e:
            print(e)

    @staticmethod
    def job1():
        print(threading.current_thread().getName())
        try:
            requests.get('http://www.google.com')
        except Exception as e:
            print(e)



if __name__ == '__main__':
    inc = 1
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, ServiceRun.perform_command, (inc,))
    # schedule.enter(inc, 0, ServiceRun.perform_command, (inc,))

    # 持续运行，直到计划时间队列变成空为止
    schedule.run()
