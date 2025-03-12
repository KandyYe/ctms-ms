#!/usr/bin/env python
# encoding: utf-8

# @version: v1.0
# @author:  Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file:    main.py
# @time:    星期三 2025/3/5 15:33

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from application import settings
from application import urls
from core.docs import custom_api_docs
from core.exception import register_exception
from core.event import lifespan
from utils.tools import import_modules


def start_gateway():
    """
    启动项目
    docs_url：配置交互文档的路由地址，如果禁用则为None，默认为 /docs
    redoc_url： 配置 Redoc 文档的路由地址，如果禁用则为None，默认为 /redoc
    openapi_url：配置接口文件json数据文件路由地址，如果禁用则为None，默认为/openapi.json
    """
    app = FastAPI(
        title="ctms-gateway",
        description="Cryptocurrency Trading Management System",
        version=settings.VERSION,
        lifespan=lifespan,
        docs_url=None,
        redoc_url=None
    )
    import_modules(settings.MIDDLEWARES, "中间件", app=app)
    # 全局异常捕捉处理
    register_exception(app)
    # 跨域解决
    if settings.CORS_ORIGIN_ENABLE:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOW_ORIGINS,
            allow_credentials=settings.ALLOW_CREDENTIALS,
            allow_methods=settings.ALLOW_METHODS,
            allow_headers=settings.ALLOW_HEADERS
        )

    # 引入应用中的路由
    for url in urls.urlpatterns:
        app.include_router(url["ApiRouter"], prefix=url["prefix"], tags=url["tags"])

    # 配置接口文档静态资源
    custom_api_docs(app)
    return app

def main():
    uvicorn.run(app='main:start_gateway', host='0.0.0.0', port=9000, lifespan="on", factory=True)


if __name__ == '__main__':
    main()
