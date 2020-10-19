from apps.extensions import db
import logging
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    user_code = db.Column(db.String(100))
    # 根据生成密码的规则，password代表的是密码hash，并非明文密码
    password = db.Column(db.String(100))


    @property
    # property包装器表明将函数直接当作属性使用
    # 必须如此声明，此可以使用_password包装器
    # 以及使用setter和getter方法
    def _password(self):
        return self.password

    @_password.setter
    def _password(self,password):
        self.password = generate_password_hash(password)
        # self.save()


    def check_password(self,password):
        return check_password_hash(self.password,password)

    @classmethod
    def create(cls,**kwargs):
        try:
            obj = cls(user_code=kwargs.get('user_code'))
            if kwargs.get('password'):
                obj.password = kwargs.get('password')
            else:
                # 使用=，调用的是_password.setter方法
                obj._password = '123456'

            db.session.add(obj)
            db.session.commit()
            return obj

        except Exception as e:
            logging.debug(e)


class Admin(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    user_code = db.Column(db.String(100))
    # 根据生成密码的规则，password代表的是密码hash，并非明文密码
    password = db.Column(db.String(100))


    @property
    # property包装器表明将函数直接当作属性使用
    # 必须如此声明，此可以使用_password包装器
    # 以及使用setter和getter方法
    def _password(self):
        return self.password

    @_password.setter
    def _password(self,password):
        self.password = generate_password_hash(password)
        # self.save()


    def check_password(self,password):
        return check_password_hash(self.password,password)

    @classmethod
    def create(cls,**kwargs):
        try:
            obj = cls(user_code=kwargs.get('user_code'))
            if kwargs.get('password'):
                obj.password = kwargs.get('password')
            else:
                # 使用=，调用的是_password.setter方法
                obj._password = '123456'

            db.session.add(obj)
            db.session.commit()
            return obj

        except Exception as e:
            logging.debug(e)


# a = {'user_code':'167632'}
# User.create(**a)

