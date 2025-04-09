#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author: Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file: __init__.py
# @time: 2025/2/8 16:22

from .mongo_manage import MongoManage

db = MongoManage()


def get_database() -> MongoManage:
    return db
