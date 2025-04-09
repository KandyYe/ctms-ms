#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author: Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file: utils.py
# @time: 星期日 2025/2/9 11:39

from datetime import datetime, timedelta,date

def today_8am_timestamp():
    # 获取今天的日期
    today = datetime.now().date()

    # 创建一个表示今天8:00的datetime对象
    eight_oclock = datetime.combine(today, datetime.min.time()) + timedelta(hours=8)

    # 将datetime对象转换为时间戳
    timestamp = int(eight_oclock.timestamp())

    return timestamp

def yesterday_8am_timestamp():
    # 获取今天的日期
    yesterday = date.today() - timedelta(days=1)

    # 创建一个表示今天8:00的datetime对象
    eight_oclock = datetime.combine(yesterday, datetime.min.time()) + timedelta(hours=8)

    # 将datetime对象转换为时间戳
    timestamp = int(eight_oclock.timestamp())

    return timestamp