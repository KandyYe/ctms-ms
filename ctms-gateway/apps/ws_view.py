#!/usr/bin/env python  
# encoding: utf-8

# @version: v1.0
# @author:  Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file:    ws_view.py
# @time:    星期三 2025/3/5 15:33


from fastapi import APIRouter, Depends, Request, Body, WebSocket
from application.settings import CTMS_DB_WS_URL, CTMS_CORE_WS_URL
from fastapi import Request, Response
import httpx
import asyncio
from .auth import verify_token

app = APIRouter()

# 添加WebSocket转发路由
@app.websocket("/ws/{service_name}/{path:path}", dependencies=[Depends(verify_token)])
async def websocket_proxy(websocket: WebSocket, service_name: str, path: str):
    # 定义目标服务地址
    SERVICES = {
        "core": CTMS_CORE_WS_URL,
        "db": CTMS_DB_WS_URL
    }

    if service_name not in SERVICES:
        await websocket.close(code=1008, reason="Service not found")
        return

    target_url = f"{SERVICES[service_name]}/{path}"

    # 连接到目标WebSocket服务
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", target_url) as target_ws:
            # 接受客户端连接
            await websocket.accept()

            # 双向消息转发
            async def forward_to_client():
                async for message in target_ws.aiter_text():
                    await websocket.send_text(message)

            async def forward_to_target():
                async for message in websocket.iter_text():
                    await target_ws.send_text(message)

            await asyncio.gather(
                forward_to_client(),
                forward_to_target()
            )