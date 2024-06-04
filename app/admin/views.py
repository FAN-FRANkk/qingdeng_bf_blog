from flask import Blueprint, render_template
from .models import User

# 实例化蓝图
bp = Blueprint('admin', __name__, url_prefix='/bf_admin', template_folder='templates', static_folder='static')


@bp.route('/login')
def login():
    return 'login page for administrator'

@bp.route('/index')
def index():
    return render_template('admin_child_1/index.html')