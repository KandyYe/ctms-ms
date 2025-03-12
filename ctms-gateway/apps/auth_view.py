#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author:  Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file:    views.py
# @time:    星期三 2025/3/5 15:33

from fastapi import APIRouter
from application.settings import CTMS_DB_REST_URL
from fastapi import Request, Response
import httpx

app = APIRouter()


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    url = f"{CTMS_DB_REST_URL}/auth/{path}"
    if len(request.query_params) != 0:
        url = f"{url}?{request.query_params}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers={key: value for key, value in request.headers.items() if key!= "host"},
            data=await request.body(),
            cookies=request.cookies
        )
        return Response(content=response.content, status_code=response.status_code, headers=dict(response.headers))
