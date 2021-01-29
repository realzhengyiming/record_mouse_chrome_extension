# -*- coding=utf-8 -*-
from flask import Flask
from datetime import timedelta
import datetime
from flask_cors import *  # 导入模块


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)  # 设置跨域
    from .reduce import reduce
    app.register_blueprint(reduce)
    return app