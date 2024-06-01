from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 实例化
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py', silent=True)

    # 引入blog视图(这个引入必须放在create_app里
    from app.blog import views as blog
    # 注册蓝图
    app.register_blueprint(blog.bp)

    # 初始化数据库
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册模型
    from app.blog import models
    from app.admin import models

    # 注册首页的url规则
    app.add_url_rule(rule='/', endpoint='index', view_func=blog.index)

    return app



# users_blueprint = Blueprint('start', __name__, static_folder='static')
#
# users_blueprint.add_url_rule(rule='/login', view_func=views.login)