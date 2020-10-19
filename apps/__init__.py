from apps.settings import config
from flask import Flask
import os
from apps.extensions import db,jwt
from apps.auth.auths import user_loader_handler,user_indetity_handler
from apps.user.views import user_bp

def creat_app(configkey):
    app = Flask(__name__)
    app.config.from_object(config[configkey])

    register_extensions(app)
    redister_blueprints(app)

    if not app.debug or os.environ.get('WERKZUEG_RUN_MAIN') == 'true':
        try:
            return app
        except Exception as e:
            app.logger.error('{}'.format(e))

    else:
        return app


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)

    # 初始的identity为实例本身，再次自定义user_identity_handler
    # 设置为用户的user_code
    # 另一种注册方式，查看app.py里
    # @jwt.user_identity_loader,下面自定义函数亦可
    # 两种方式均可实现自定义的identity
    jwt.user_identity_loader(user_indetity_handler)

    # 初始化注册，表示的是使用自定义的回调函数
    # 相关功能的初始化，应用调用是才会实例化
    # 初始没有当前用户，自定义返回当前的用户
    jwt.user_loader_callback_loader(user_loader_handler)

def redister_blueprints(app):
    app.register_blueprint(user_bp)
