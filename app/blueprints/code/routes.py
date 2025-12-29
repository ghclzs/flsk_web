from flask import Blueprint, request, current_app

from app.services.code.code_services import CodeServices
from app.utils.response import success, fail


code_bp = Blueprint("code", __name__, url_prefix="/code")


@code_bp.route("/login_code", methods=["GET"])
def login_code():
    phone = request.args.get("phone")
    type = request.args.get("type")
    current_app.logger.info(f"开始获取登录验证码，手机号：{phone}，类型：{type}")
    
    service = CodeServices()
    method_mapping = {
        "app": service.get_edu_app_captcha,
        "edu_c": service.get_edu_c_captcha,
        "edu_b": service.get_edu_b_captcha,
        "edu_c_test": lambda p: service.get_tset_captcha(p, "edu_c_test"),
        "c_test": lambda p: service.get_tset_captcha(p, "c_test")
    }
    
    if type in method_mapping:
        data = method_mapping[type](phone)
    else:
        return fail(msg="不支持的验证码类型")
    
    # 统一处理返回的数据格式
    if isinstance(data, dict) and 'data' in data:
        # 如果是API返回的完整格式
        if data.get('success', True) and data.get('code') == 200:
            return success(data['data'], msg=data.get('msg', '获取成功'))
        else:
            return fail(msg=data.get('msg', '获取失败'))
    elif isinstance(data, str) or data is None:
        # 如果是直接的验证码字符串或None（来自Redis方法）
        if data is not None:
            return success(data, msg="获取成功")
        else:
            return fail(msg="未找到验证码")
    else:
        return fail(msg="获取失败")


@code_bp.route("/login", methods=["GET"])
def login():
    return success(data="登录成功"
    , msg="登录成功")