from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Fylgyd123.@127.0.0.1:3306/bohou?charset=utf8mb4"
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "tb_student"
    id = db.Column(db.Integer, primary_key=True, comment="学号")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.Integer, comment="性别")


if __name__ == '__main__':
    # 谨慎使用此语句，这会直接删除项目中所有模型对应的表
    # 执行流程是: 先找本项目中的所有模型，再去MySQL比对，找到则删除
    with app.app_context():
        db.drop_all()
    app.run(debug=True)