#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: canheting 
@software: PyCharm 
@file: models.py 
@time: 2019/8/17 11:17 
@description：
"""
from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.DateTime, default=datetime.now)
    telphone = db.Column(db.String(11), nullable=True)


class Question(db.Model):
    __tablename__ = 'question'
    id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('question'))
