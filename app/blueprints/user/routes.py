from flask import Blueprint, request
from app.models.user import User
from app.utils.response import success, fail
from app.extensions import verify_token

user_bp = Blueprint("user", __name__, url_prefix="/user")

# 登录校验装饰器
def login_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return fail(msg="请先登录", code=401)
        # 去除Bearer前缀（如果有）
        if token.startswith("Bearer "):
            token = token[7:]
        user_id = verify_token(token)
        if not user_id:
            return fail(msg="token过期或无效", code=401)
        # 将用户ID传入视图函数
        kwargs["user_id"] = user_id
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@user_bp.route("/info", methods=["GET"])
@login_required
def get_user_info(user_id):
    """获取当前登录用户信息"""
    user = User.query.get(user_id)
    if not user:
        return fail(msg="用户不存在", code=404)
    return success(data=user.to_dict())

@user_bp.route("/list", methods=["GET"])
@login_required
def get_user_list(user_id):
    """获取用户列表（示例）"""
    users = User.query.all()
    user_list = [user.to_dict() for user in users]
    return success(data=user_list)