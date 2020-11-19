from apps.models import User,Admin
import logging

# import cairosvg

def user_loader_handler(indentity=None):
    if indentity is None:
        return None
    # 返回当前的认证的用户
    # 需要修改jwt的indentity为用户的user_code
    # mongo的写法
    # user = User.objects(user_code=indentity).first()
    # mysql的写法
    try:
        # 当有不同的用户角色时候，使用此种方式,传入当前的用户角色
        user = User.query.filter_by(user_code=indentity).first()
        if user:
            current_user = user
            return current_user
        else:
            admin = Admin.query.filter_by(user_code=indentity).first()
            current_user = admin
            return current_user
    except Exception as e:
        logging.debug(e)

def user_indetity_handler(instance):
    return instance.user_code