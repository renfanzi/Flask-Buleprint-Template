#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask.ext.script import Manager  # 启动管理模块，可以使用shell等方式（属于扩展包）
from livereload import Server  # 如果要时时刷新，免去F5，就可以安装livereload
from movie_flask import create_app

app = create_app()
# app.listen(port=5001)
manager = Manager(app)


@manager.command
def dev():
    live_server = Server(app.wsgi_app)
    # live_server.watch('static/*.*') #检测的目录  如果是项目里面目录（'**/*.*'）
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)


if __name__ == '__main__':
    # app.run(debug=True)
    # manager.run()
    dev()
    # 启动的时候就是python run.py runserver
