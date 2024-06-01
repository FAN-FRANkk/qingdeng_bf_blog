# 导入flask核心类
from flask import Flask

# 初始化web应用程序的实例对象
app = Flask(__name__)
"""flask项目加载配置项，一"""
# app.config['配置项'] = 配置项的值
# app.config['DEBUG'] = True

"""二"""
config = {
    'DEBUG': True
}
app.config.update(config)

"""三"""
# from settings_1 import Setting
# app.config.from_object(Setting)

"""四"""
# 这个时候文件里直接就是代码，没有定义类
# app.config.from_pyfile('setting_1.py')


# 通过实例对象app提供的route路由装饰器，绑定试图与url地址的关系
@app.route("/goods/<gid>/<rid>")
def index(gid, rid):
    print(gid, type(gid))
    print(rid, type(rid))
    # 视图的返回值将被flask包装成响应对象的HTML文档内容，返回给客户端
    return f'hello flask{gid}---{rid}'

# 自定义路由转换
# 引入基类
from werkzeug.routing.converters import BaseConverter

# 1. 自定义路由转换类
class EmailConverter(BaseConverter):
    """邮箱类型转换器"""
    regex = r'[a-zA-Z0-9_-]+'
    # regex = r'^[\w\.-]+@[\w\.-]+\.\w+'

app.url_map.converters['email']= EmailConverter

# 使用自定义路由转换器
@app.route('/email/<email:email>')
def email(email):
    return "send email to {}".format(email)

if __name__ == '__main__':
    # 启动flask的app
    app.run()

