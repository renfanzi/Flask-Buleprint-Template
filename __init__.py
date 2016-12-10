#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.routing import BaseConverter  # 针对url正则
from werkzeug.utils import secure_filename  # 针对安全文件名
from flask.ext.script import Manager    #启动管理模块，可以使用shell等方式（属于扩展包）
from livereload import Server   #如果要时时刷新，免去F5，就可以安装livereload


class RegexConverter(BaseConverter):
    """
    URL正则扩展类
    """

    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

def create_app():

    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter  # 扩展调用方法
    from movie_flask.app.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main', static_folder='static', template_folder='templates',)  #意思是可以在建立一个static

    return app






