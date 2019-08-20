#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: canheting
@software: PyCharm
@file: manage.py
@time: 2019/8/18 21:33
@description：
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import User, Question

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
