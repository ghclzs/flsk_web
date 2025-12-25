from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.extensions import db  # 关联全局的db对象



# 定义 Model
class Student(db.Model):
    # 对应数据库表名（如果表名不是默认的小写类名，需要显式指定）
    __tablename__ = "student"  # 假设你的表名是student，根据实际情况修改

    # 匹配数据库字段：学生学号（主键、自增）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="学生学号（主键）")
    # 匹配数据库字段：学生姓名（非空）
    name = db.Column(db.String(20), nullable=False, comment="学生姓名")
    # 匹配数据库字段：学生性别（枚举类型，默认值'男'）
    gender = db.Column(db.Enum('男', '女'), default='男', comment="学生性别")
    # 匹配数据库字段：学生年龄（tinyint，范围10-100）
    age = db.Column(db.Integer, comment="学生年龄（10-100）")
    # 匹配数据库字段：班级名称
    class_name = db.Column(db.String(30), comment="班级名称")  # 注意：数据库字段是class_name（下划线），避免与Python关键字冲突
    # 匹配数据库字段：入学日期
    admission_date = db.Column(db.Date, comment="入学日期")

    # 转换为字典（接口返回时用，包含所有字段）
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'class_name': self.class_name,
            'admission_date': self.admission_date.strftime("%Y-%m-%d") if self.admission_date else None  # 日期格式化为字符串
        }