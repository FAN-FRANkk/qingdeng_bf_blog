from flask import Blueprint, render_template
from .models import Post

bp = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates', static_folder='static')

# @bp.route('/index')
def index():

    return render_template('index.html', **locals())


