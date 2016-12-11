# Flask-Buleprint-Template
This is my Python Flask Long Architecture
这个是flask 的blutprint 的一个大型框架的一个轮子
避免自己重复的造轮子
同时说一下启动文件，有两个启动文件

manage.py
```python
启动方式1：ide直接右键运行dev()
启动方式2：python3 manage.py runserver
```
而run.py 是以脚本形式，懒惰的写在了一个里面，方便对比
<<<<<<< HEAD

通常写cookie的时候需要make_response  进行包装

最后注意一个地方就是蓝图里面的api装饰器
其次是注意一点：在写接口的时候想跳转到例如index接口上面等类似写法
```python
@main.route('/usr/<regex("[a-z]{3}"):user_id>')
# 正则扩展方法展示
def user_id(user_id):
    # return user_id
    return redirect(url_for('main.hello_world'))  # 看这里跳转的时候是方法名需要注意了


@main.route('/index')
def hello_world():
    """这里注意文件夹的名字是templates"""
    response = make_response(render_template("index.html", title="!!!!asdfasdf"))

    response.set_cookie('username', '')  # 设置cookie
    return response

```

=======
通常写cookie的时候需要make_response  进行包装
最后注意一个地方就是蓝图里面的api装饰器
其次是注意一点：在写接口的时候是mian.index等类似写法
>>>>>>> 9985b91b773eba3664ef4a594324c5b4fb03efe5


![img](https://github.com/renfanzi/Flask-Buleprint-Template/blob/master/readme_img/flask_view_api.png)
