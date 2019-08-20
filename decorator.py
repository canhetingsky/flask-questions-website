#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: canheting 
@software: PyCharm 
@file: decorator.py 
@time: 2019/8/16 12:24 
@description：
"""
from functools import wraps
from flask import session, redirect, url_for


# 登录限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
