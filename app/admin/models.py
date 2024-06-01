from start import db
from datetime import datetime

class BaseModel(db.Model):
    """基类模型"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, comment='id_primary')
    add_time = db.Column(db.DateTime, default=datetime.now(), comment='create time')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='update time')

class User(BaseModel):
    """帖子模型"""
    __tablename__ = 'tb_user'
    username = db.Column(db.String(64), unique=True, comment='username')
    password = db.Column(db.String(128), comment='password')
    last_login = db.Column(db.DateTime, comment='last login time')
    nickname = db.Column(db.String(64), comment='nickname')
    avatar_path = db.Column(db.String(128), comment='avatar path')
    posts = db.relationship('Post', backref='post_user')
    notes = db.relationship('Note', backref='note_user')

class BlogInfo(BaseModel):
    """网站信息"""
    __tablename__ = 'tb_bolg_info'
    title = db.Column(db.String(64), comment='title for website')
    subtitle = db.Column(db.String(64), comment='subtitle for website')
    about_me = db.Column(db.Text, comment='about me')



