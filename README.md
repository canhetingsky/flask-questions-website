

## 项目文件说明

- .idea: pycharm工程文件
- migrations: 数据库管理文件夹
- static: flask的静态文件夹
  - css: css样式文件夹
  - images: 图片文件夹
  - js: js脚本文件夹
- templates: flask的模板文件夹
- tmp: sqlite的数据库文件夹
- app.py flask启动文件
- config.py flask配置文件
- decorator.py 装饰器文件
- exts.py 中间件文件，防止循环引用
- manage.py 数据库迁移扩展脚本
- models.py flask数据库映射对象
- README.md 项目说明文件
- test_interface.py 接口测试文件

## 安装项目依赖的库

`pip install -r requirements.txt`

## 数据库管理脚本`manage.py`

1. 初始化，运行命令 `python manage.py db init`，生成migrations文件夹
2. 迁移文件，运行命令 `python manage.py db migrate`，在`versions`文件夹下生成迁移文件
3. 映射到数据库（升级），运行命令 `python manage.py db upgrade` ,创建或者更新数据库

## 运行网站

运行命令`python app.py`，然后浏览器打开<http://127.0.0.1:5000/>查看

