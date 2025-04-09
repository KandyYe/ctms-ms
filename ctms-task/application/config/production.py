#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author: Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file: production.py
# @time: 2025/2/8 16:22

"""
Redis 数据库配置
"""
REDIS_DB_ENABLE = True
REDIS_DB_URL = "redis://127.0.0.1:6379/2"

"""
MongoDB 数据库配置
"""
MONGO_DB_ENABLE = True
MONGO_DB_NAME = "ctms"
MONGO_DB_URL = f"mongodb://127.0.0.1:27017/?authSource={MONGO_DB_NAME}"
