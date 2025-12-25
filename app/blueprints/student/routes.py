from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models.student import Student

from app.utils.response import success, fail


student_bp = Blueprint("student", __name__, url_prefix="/student")


@student_bp.route("/get_detail/<int:stu_id>", methods=["GET"])
def studet_detail(stu_id):
    try:
        student = Student.query.get(stu_id)
        if not student:
            return fail(msg=f"未找到ID为{stu_id}的学生")
        return success(data=student.to_dict(), msg="查询成功")
    except SQLAlchemyError as e:
        return fail(msg=f"查询失败：{str(e)}")


# 1.2 学生列表（支持分页、姓名模糊查询）
@student_bp.route("/list", methods=["GET"])
def student_list():
    try:
        # 获取分页和查询参数
        page = request.args.get("page", 1, type=int)
        size = request.args.get("size", 10, type=int)
        name = request.args.get("name", "")

        # 构建查询条件
        query = Student.query
        if name:
            query = query.filter(Student.name.like(f"%{name}%"))

        # 执行分页查询
        paginate = query.order_by(Student.id.desc()).paginate(page=page, per_page=size)

        # 组装返回数据
        data = {
            "total": paginate.total,  # 总条数
            "pages": paginate.pages,  # 总页数
            "current_page": page,
            "list": [stu.to_dict() for stu in paginate.items]
        }
        return success(data=data, msg="列表查询成功")
    except SQLAlchemyError as e:
        return fail(msg=f"列表查询失败：{str(e)}")


# ====================== 2. 新增接口 ======================
@student_bp.route("/add", methods=["POST"])
def add_student():

    try:
        # 获取请求参数
        req_data = request.get_json()
        if not req_data:
            return fail(msg="请求参数不能为空")

        # 基础参数校验
        name = req_data.get("name")
        age = req_data.get("age", 0)
        if not name:
            return fail(msg="学生姓名不能为空")
        if not isinstance(age, int) or age <= 0:
            return fail(msg="年龄必须为正整数")

        # 创建学生实例
        new_student = Student(
            name=name,
            age=age,
            gender=req_data.get("gender", "男"),  # 默认值
            class_name=req_data.get("class_name", ""),
            admission_date=req_data.get("admission_date")
        )

        # 提交数据库
        db.session.add(new_student)
        db.session.commit()
        return success(data=new_student.to_dict(), msg="新增学生成功")
    except SQLAlchemyError as e:
        db.session.rollback()  # 异常回滚
        return fail(msg=f"新增失败：{str(e)}")


@student_bp.route("/update", methods=["POST"])
def update_student():
    try:
        req_data = request.get_json()
        stu_id = req_data.get("stu_id")
        # 查询学生是否存在
        student = Student.query.get(stu_id)
        if not student:
            return fail(msg=f"未找到ID为{stu_id}的学生")

        # 获取修改参数
        req_data = request.get_json()
        if not req_data:
            return fail(msg="修改参数不能为空")

        # 按需更新字段（只更新传入的参数）
        if "name" in req_data:
            student.name = req_data["name"]
        if "age" in req_data and isinstance(req_data["age"], int) and req_data["age"] > 0:
            student.age = req_data["age"]
        if "gender" in req_data:
            student.gender = req_data["gender"]
        if "class_name" in req_data:
            student.class_name = req_data["class_name"]
        if "admission_date" in req_data:
            student.admission_date = req_data["admission_date"]

        # 提交修改
        db.session.commit()
        return success(data=student.to_dict(), msg="修改学生信息成功")
    except SQLAlchemyError as e:
        db.session.rollback()
        return fail(msg=f"修改失败：{str(e)}")


@student_bp.route("/delete", methods=["GET"])
def delete_student():
    try:
        stu_id = request.args.get("stu_id")
        # 查询学生
        student = Student.query.get(stu_id)
        if not student:
            return fail(msg=f"未找到ID为{stu_id}的学生")

        # 删除并提交
        db.session.delete(student)
        db.session.commit()
        return success(msg=f"删除ID为{stu_id}的学生成功")
    except SQLAlchemyError as e:
        db.session.rollback()
        return fail(msg=f"删除失败：{str(e)}")


