from flask import Blueprint, render_template, request
from .models import User
from app.blog.models import Category
from start import db

# 实例化蓝图
bp = Blueprint('admin', __name__, url_prefix='/bf_admin', template_folder='templates', static_folder='static')


@bp.route('/login')
def login():
    return 'login page for administrator'

@bp.route('/index')
def index():
    return render_template('admin_child_1/common/index.html')

@bp.route('/post')
def post():
    return render_template('admin_child_1/common/post.html')

# 分类管理页
@bp.route('/category')
def category():
    return render_template('admin_child_1/common/category.html')

@bp.route('/category_add', methods=['post'])
def category_add():
    category_name = request.form['value']
    category_name_exist = Category.query.filter_by(name=category_name).first()
    if not category_name_exist:
        category_obj = Category(name=category_name_exist)
        db.session.add(category_obj)
        db.session.commit()
        return 'success'
    return 'existed'


# 标签管理页
@bp.route('/tag')
def tag():
    return render_template('admin_child_1/common/tag.html')