#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: canheting 
@software: PyCharm 
@file: config.py 
@time: 2019/8/14 19:31 
@description：
"""
import os
from datetime import timedelta

DEBUG = False
SECRET_KEY = os.urandom(24)
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True