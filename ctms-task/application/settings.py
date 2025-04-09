#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author: Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file: settings.py
# @time: 2025/2/8 16:22

import os

"""项目根目录"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True


"""
引入数据库配置
"""
if DEBUG:
    from application.config.development import *
else:
    from application.config.production import *


"""
发布/订阅通道
"""
SUBSCRIBE = 'ctms_task_queue'


"""
MongoDB 集合
"""
# 用于存放任务调用日志
SCHEDULER_TASK_RECORD = "scheduler_task_record"
# 用于存放运行中的任务
SCHEDULER_TASK_JOBS = "scheduler_task_jobs"
# 用于存放任务信息
SCHEDULER_TASK = "crypto_system_task"

# 数据库url
CTMS_DB_URL = "http://127.0.0.1:9001/"

"""
定时任务脚本目录
"""
TASKS_ROOT = "tasks"
