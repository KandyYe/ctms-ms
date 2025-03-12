#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author:  Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file:    ws_view.py
# @time:    星期三 2025/3/5 15:33


from apps.views import app as ctms_app
from apps.ws_view import app as crypto_ws_app
from apps.auth_view import app as auth_app


# 引入应用中的路由
urlpatterns = [
    {"ApiRouter": auth_app, "prefix": "/auth", "tags": ["系统认证"]},
    {"ApiRouter": crypto_ws_app, "prefix": "/crypto/ws", "tags": ["交易websocket"]},
    {"ApiRouter": ctms_app, "prefix": "", "tags": ["ctms"]},
]
