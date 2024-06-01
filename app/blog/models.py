from start import db
from datetime import datetime

class BaseModel(db.Model):
    """ 基类模型 """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, comment='id_primary')
    add_time = db.Column(db.DateTime, default=datetime.now(), comment='create time')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='update time')


post_tag = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('tb_post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tb_tag.id'), primary_key=True)
)

note_tag = db.Table(
    'note_tags',
    db.Column('note_id', db.Integer, db.ForeignKey('tb_note.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tb_tag.id'), primary_key=True)
)

class Post(BaseModel):
    """文章模型"""
    __tablename__ = 'tb_post'
    title = db.Column(db.String(256), comment='title')
    cover = db.Column(db.String(512), comment='cover')
    content_md = db.Column(db.Text, comment='content markdown')
    content_html = db.Column(db.Text, comment='content html')
    read_count = db.Column(db.Integer, default=0, comment='read count')
    draft_flag = db.Column(db.Boolean, default=False, comment='is draft')
    category_id = db.Column(db.Integer, db.ForeignKey('tb_category.id'), comment='category id')
    tags = db.relationship('Tag', secondary=post_tag, backref='tag_post')
    comments = db.relationship('Comment', backref='comment_post', cascade='delete')
    attachments = db.relationship('Attachment', backref='attach_post')
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'), comment='user id')

class Category(BaseModel):
    """ 分类表 """
    __tablename__ = 'tb_category'
    name = db.Column(db.String(64), unique=True, comment='category name')
    posts = db.relationship('Post', backref='post_category')
    notes = db.relationship('Note', backref='note_category')

class Tag(BaseModel):
    """ 标签表 """
    __tablename__ = 'tb_tag'
    name = db.Column(db.String(64), unique=True, comment='tag name')
    color = db.Column(db.String(32), comment='tag color')



class Note(BaseModel):
    """ 笔记表 """
    __tablename__ = 'tb_note'
    title = db.Column(db.String(256), comment='title')
    content_md = db.Column(db.Text, comment='content markdown')
    content_html = db.Column(db.Text, comment='content html')
    read_count = db.Column(db.Integer, default=0, comment='read count')
    category_id = db.Column(db.Integer, db.ForeignKey('tb_category.id'), comment='category id')
    tags = db.relationship('Tag', secondary=note_tag, backref='tag_note')
    attachments = db.relationship('Attachment', backref='attach_note')
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'), comment='user id')

class Comment(BaseModel):
    """ 评论表 """
    __tablename__ = 'tb_comment'
    content = db.Column(db.Text, comment='comment content')
    visitor_name = db.Column(db.String(64), comment='visitor name')
    visitor_email = db.Column(db.String(64), comment='visitor email')
    visitor_ip = db.Column(db.String(65), comment='visitor ip')
    visitor_address = db.Column(db.String(32), comment='visitor address')
    post_id = db.Column(db.Integer, db.ForeignKey('tb_post.id'))
    replied_id = db.Column(db.Integer, db.ForeignKey('tb_comment.id'), comment='回复的评论id')
    replied = db.relationship('Comment', backref='replies', cascade='delete')

class Message(BaseModel):
    """ 留言表 """
    __tablename__ = 'tb_message'
    content = db.Column(db.Text, comment='comment content')
    visitor_name = db.Column(db.String(64), comment='visitor name')
    visitor_email = db.Column(db.String(64), comment='visitor email')
    visitor_ip = db.Column(db.String(65), comment='visitor ip')
    visitor_address = db.Column(db.String(32), comment='visitor address')


class Attachment(BaseModel):
    """ 附件表 """
    __tablename__ = 'tb_attachment'
    file_name = db.Column(db.String(256), comment='file name')
    file_size = db.Column(db.String(32), comment='file size')
    file_path = db.Column(db.String(256), comment='file path')
    post_id = db.Column(db.Integer, db.ForeignKey('tb_post.id'), comment='post id')
    note_id = db.Column(db.Integer, db.ForeignKey('tb_note.id'), comment='note id')

