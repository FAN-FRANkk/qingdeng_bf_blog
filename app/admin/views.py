from flask import Blueprint, render_template, request, jsonify
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
    """ 分类管理API"""
    return render_template('admin_child_1/common/category.html')

@bp.route('/category_query')
def category_query():
    """ 分类管理—查询API"""
    page = request.args.get('page', type=int, default=1)
    limit = request.args.get('limit', type=int, default=5)
    category_pg = Category.query.paginate(page=page, per_page=limit)
    category_list = []
    for item in category_pg.items:
        row = {
            'id': item.id,
            'name': item.name,
            'add_time': item.add_time,
            'modify_time': item.update_time
        }
        category_list.append(row)
        # layui需要的表格数据解析回调的格式
    data = {
        'code': 0,
        'data': category_list,  # 实际数据
        'count': category_pg.total,  # 数据总数
        'msg': ''
    }
    return jsonify(data)


@bp.route('/category_add', methods=['post'])
def category_add():
    category_name = request.form['value']
    category_name_exist = Category.query.filter_by(name=category_name).first()
    if not category_name_exist:
        category_obj = Category(name=category_name)
        db.session.add(category_obj)
        db.session.commit()
        return 'success'
    return 'existed'


# 标签管理页
@bp.route('/tag')
def tag():
    return render_template('admin_child_1/common/tag.html')