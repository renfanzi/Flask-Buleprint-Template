#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, make_response
from . import main
from . import main_api
from flask_restful import Resource


@main.route('/usr/<regex("[a-z]{3}"):user_id>')
# 正则扩展方法展示
def user_id(user_id):
    # return user_id
    return redirect(url_for('main.hello_world'))  # 看这里跳转的时候是方法名需要注意了


@main_api.resource('/userapi/')
class user(Resource):
    @staticmethod
    def get():
        user_id = request.args.get("user_id")
        return user_id


@main.route('/index')
def hello_world():
    """这里注意文件夹的名字是templates"""
    response = make_response(render_template("index.html", title="!!!!asdfasdf"))

    response.set_cookie('username', '')  # 设置cookie
    return response
    # return "hello"
