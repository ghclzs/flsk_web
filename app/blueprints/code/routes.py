from flask import Blueprint, request, current_app

from app.services.code.code_services import CodeServices
from app.utils.response import success, fail


code_bp = Blueprint("code", __name__, url_prefix="/code")


@code_bp.route("/login_code", methods=["GET"])
def login_code():
    phone = request.args.get("phone")
    type = request.args.get("type")
    current_app.logger.info(f"开始获取登录验证码，手机号：{phone}，类型：{type}")
    if type == "app":
        data = CodeServices().get_edu_app_captcha(phone)
    if type == "edu_c":
        data = CodeServices().get_edu_c_captcha(phone)
    if type == "edu_b":
        data = CodeServices().get_edu_b_captcha(phone)
    return success(data['data'], msg="获取成功")


@code_bp.route("/login", methods=["GET"])
def login():
    return success(data="登录成功"
    , msg="登录成功")