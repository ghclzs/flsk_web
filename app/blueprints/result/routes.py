from flask import Blueprint, request, current_app
from sqlalchemy.exc import SQLAlchemyError

from app.models.result import Api_test_report_results

from app.utils.response import success, fail

result_bp = Blueprint("result", __name__, url_prefix="/result")


@result_bp.route("/get_detail/<int:id>", methods=["GET"])
def result_detail(id):
    current_app.logger.info(f"开始获取测试结果详情，ID：{id}")
    try:
        result = Api_test_report_results.query.get(id)
        if not result:
            current_app.logger.warning(f"未找到ID为{id}的测试结果")
            return fail(msg=f"未找到ID为{id}的测试结果")

        current_app.logger.info(f"测试结果详情查询成功，ID：{id}，内容：{result.to_dict()}")
        return success(data=result.to_dict(), msg="查询成功")
    except SQLAlchemyError as e:
        current_app.logger.error(f"查询测试结果详情失败，ID：{id}，错误：{str(e)}", exc_info=True)
        return fail(msg=f"查询失败：{str(e)}")


# ====================== 2. 查询列表（支持分页/筛选） ======================
@result_bp.route("/list", methods=["GET"])
def result_list():
    current_app.logger.info("开始查询测试结果列表")
    try:
        # 获取分页/筛选参数（从URL参数中获取，如 /result/list?page=1&size=10&project_name=测试项目）
        page = request.args.get("page", 1, type=int)
        size = request.args.get("size", 10, type=int)
        project_name = request.args.get("project_name", "")  # 按项目名称筛选

        # 构建查询条件
        query = Api_test_report_results.query
        if project_name:
            query = query.filter(Api_test_report_results.project_name.like(f"%{project_name}%"))

        # 分页查询
        pagination = query.order_by(Api_test_report_results.id.desc()).paginate(page=page, per_page=size,
                                                                                error_out=False)
        result_list = [item.to_dict() for item in pagination.items]

        # 构造返回数据
        data = {
            "list": result_list,
            "total": pagination.total,  # 总条数
            "page": page,  # 当前页
            "size": size,  # 每页条数
            "pages": pagination.pages  # 总页数
        }
        current_app.logger.info(f"测试结果列表查询成功，总数：{pagination.total}，当前页：{page},列表信息：{result_list}")
        return success(data=data, msg="列表查询成功")
    except SQLAlchemyError as e:
        current_app.logger.error(f"查询测试结果列表失败，错误：{str(e)}", exc_info=True)
        return fail(msg=f"列表查询失败：{str(e)}")