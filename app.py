from flask import Flask
from apps import creat_app
from apps.extensions import db
from apps.models import User,Admin
from apps.extensions import jwt
from apps.settings import DevelopConfig, BaseConfig
from flask.helpers import get_debug_flag
import cairosvg



# app = Flask(__name__)
# Config = DevelopConfig if get_debug_flag() else BaseConfig
app = creat_app('developconfig')


@app.route('/')
def hello_world():
    # cairosvg.svg2pdf()
    return "hello"

# 若想要在终端调用各个模型，需要引入这个上下文的包装器
# 直接从文件导入模型，相关的功能可能不生效
# 比如从apps.extensions import db
# db在终端测试，调用db.session.add()会报错
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User,Admin=Admin)

# @jwt.user_identity_loader
# def user_indetity_handler(instance):
#     return instance.user_code


if __name__ == '__main__':
    app.run()
