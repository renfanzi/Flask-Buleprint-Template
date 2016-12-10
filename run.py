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


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter  # 扩展调用方法
manager = Manager(app)


@app.route('/usr/<regex("[a-z]{3}"):user_id>')
# """正则扩展方法展示"""
def user(user_id):
    return user_id


@app.route('/')
def hello_world():
    """这里注意文件夹的名字是templates"""
    response = make_response(render_template("index.html", title="!!!!asd"))

    response.set_cookie('username', '')  # 设置cookie
    return response
    # return "hello"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        """这里是采用form验证的方式，所以这么写，对应前端的name=user"""
        user = request.form['user']
        file = request.files['file']  # 获取文件的方式
        path = ''
        file.save(path, secure_filename(file.filename))
    else:
        """这里是get方式"""
        user = request.args['user']
    return render_template('login.html', method=request.method)


@app.errorhandler(404)
def page_not_found(error):
    # 自定义404
    return render_template('404.html'), 404




@manager.command
def dev():
    live_server = Server(app.wsgi_app)
    #live_server.watch('static/*.*') #检测的目录  如果是项目里面目录（'**/*.*'）
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)




if __name__ == '__main__':
    # app.run(debug=True)
    # manager.run()
#启动的时候就是python run.py runserver
    dev()