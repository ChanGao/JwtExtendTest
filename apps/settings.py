import os
import datetime


class BaseConfig:
    # mysql 连接配置
    # 配置方法1
    # DIALECT = 'mysql'
    # DRIVER = 'pymysql'
    # USERNAME = 'root'
    # HOST = '127.0.0.1'
    # PASSWORD = '123456'
    # PORT = '3306'
    # DATABASE = 'testjwt'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    #     DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE
    # )

    # 必须设置SECRET_KEY
    SECRET_KEY = os.urandom(24)

    # JWT相关配置

    JWT_AUTH_USER_CODE_KEY = 'user_code'
    JWT_AUTH_PASSWORD_KEY = 'password'
    # 必须配置，不然get_csrf_token会出错
    JWT_TOKEN_LOCATION = ['cookies']
    # 默认开启，值为True
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_IN_COOKIES = False
    # 默认值为如此，可以不设置
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_REFRESH_COOKIE_PATH = '/'
    # Headers里携带这两个参数的名称
    # access_csrf,refresh_csrf
    JWT_ACCESS_CSRF_HEADER_NAME = 'x_access_csrf_token'
    JWT_REFRESH_CSRF_HEADER_NAME = 'x_refresh_csrf_token'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=120)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)

    # 配置u方法2
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/testjwt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopConfig(BaseConfig):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


config = {'developconfig': DevelopConfig}
