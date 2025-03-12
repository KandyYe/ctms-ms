#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author:  Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file:    event.py
# @time:    星期三 2025/3/5 15:33

from fastapi import FastAPI
from redis import asyncio as aioredis
from redis.exceptions import AuthenticationError, TimeoutError, RedisError
from contextlib import asynccontextmanager
from utils.tools import import_modules_async
from application.settings import REDIS_DB_URL, EVENTS


@asynccontextmanager
async def lifespan(app: FastAPI):
    await import_modules_async(EVENTS, "全局事件", app=app, status=True)

    yield

    await import_modules_async(EVENTS, "全局事件", app=app, status=False)


async def connect_redis(app: FastAPI, status: bool):
    """
    把 redis 挂载到 app 对象上面
    :param app:
    :param status:
    :return:
    """
    if status:
        rd = aioredis.from_url(REDIS_DB_URL, decode_responses=True, health_check_interval=1)
        app.state.redis = rd
        try:
            response = await rd.ping()
            if response:
                print("Redis 连接成功")
            else:
                print("Redis 连接失败")
        except AuthenticationError as e:
            raise AuthenticationError(f"Redis 连接认证失败，用户名或密码错误: {e}")
        except TimeoutError as e:
            raise TimeoutError(f"Redis 连接超时，地址或者端口错误: {e}")
        except RedisError as e:
            raise RedisError(f"Redis 连接失败: {e}")
    else:
        print("Redis 连接关闭")
        await app.state.redis.close()
