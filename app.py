#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, render_template, url_for, session, request, redirect
from models import User, Question
from exts import db
import json
from decorator import login_required

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/')
def index():
    questions = Question.query.order_by(Question.create_time.desc()).all()
    return render_template('index.html', questions=questions)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username, User.password == password).first()
        if user:
            session['user_id'] = user.id  # 本地是否登录标识
            session.permanent = True  # 有效期内不用重新登录
            return redirect(url_for('index'))
        else:
            return '用户名或者密码错误'


@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('index'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.username == username).first()
        if user:  # 判断用户名是否被占用
            return '用户名已经被注册'
        elif password1 != password2:
            return '两次密码不一致，请核对'
        else:
            user = User(username=username, password=password1)
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id  # 本地是否登录标识
            return redirect(url_for('index'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    return render_template('detail.html', question=question_id)


@app.route('/add_answer/<question_id>', methods=['POST'])
@login_required
def add_answer(question_id):
    return question_id + "评论成功"


@app.route('/search/')
def search():
    dic = {
        'name': request.args.get('q'),
        'age': request.args.get('time'),
        'day': [1, 2, 3],
        'set': {
            'settime': 2018,
            'setday': 9,
        }
    }
    return json.dumps(dic)


# 创建表格、插入数据
@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.create_all()


@app.context_processor
def app_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    else:
        return {}


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
