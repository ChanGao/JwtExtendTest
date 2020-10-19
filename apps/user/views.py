from flask import Blueprint,request,jsonify
import logging
from apps import reponses
from apps.models import User,Admin
from flask_jwt_extended import create_access_token,create_refresh_token,get_csrf_token,set_access_cookies,\
      set_refresh_cookies,unset_access_cookies,jwt_required,get_jwt_identity,current_user

user_bp = Blueprint('user_bp',__name__,url_prefix='/user/api')

@user_bp.route('/login',methods=['GET','POST'])
def login():
    """
    login user

    """
    resp_data = {}
    try :
        params = request.get_json()
        user_code = params.get('user_code')
        password = params.get('password')
        user = User.query.filter_by(user_code=user_code).first()
        admin = Admin.query.filter_by(user_code=user_code).first()
        if user:
            if user.check_password(password):
                # 记住，setting一定需要配置SECRET_KEY，否则create_access_token会报错
                access_token = create_access_token(identity=user,fresh=True)
                refresh_token = create_refresh_token(identity=user)
                return_data_dict = {
                    'role':'user',
                    'access_csrf':get_csrf_token(access_token),
                    'refresh_csrf':get_csrf_token(refresh_token)
                    # 'username':''
                }
                resp_data['code'] = reponses.SUCCESS
                resp_data['data'] = return_data_dict
                resp_data['msg'] = '登录成功'
                resp = jsonify(resp_data)
                set_access_cookies(resp,access_token)
                set_refresh_cookies(resp,refresh_token)
                return resp
            else:
                resp_data['msg'] = '密码错误'
                return jsonify(resp_data)
        elif admin:
            if admin.check_password(password):
                # 记住，setting一定需要配置SECRET_KEY，否则create_access_token会报错
                access_token = create_access_token(identity=admin,fresh=True)
                refresh_token = create_refresh_token(identity=admin)
                return_data_dict = {
                    'role':'admin',
                    'access_csrf':get_csrf_token(access_token),
                    'refresh_csrf':get_csrf_token(refresh_token)
                    # 'username':''
                }
                resp_data['code'] = reponses.SUCCESS
                resp_data['data'] = return_data_dict
                resp_data['msg'] = '登录成功'
                resp = jsonify(resp_data)
                set_access_cookies(resp,access_token)
                set_refresh_cookies(resp,refresh_token)
                return resp
            else:
                resp_data['msg'] = '密码错误'
                return jsonify(resp_data)
        else:

            resp_data['msg'] = '用户不存在'
            return jsonify(resp_data)
    except Exception as e :
        logging.debug(e)
        resp_data['msg'] = reponses.RESULT_ERROR
        return jsonify(resp_data)


@user_bp.route('/user_test',methods=['GET','POST'])
@jwt_required
def user_test():
    print(current_user)
    # 返回定义的identity
    print({'identity':get_jwt_identity()})
    return 'come in !'