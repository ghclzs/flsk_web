from flask import Blueprint, request
from app.extensions import db
from app.models.user import User
from app.utils.response import success, fail
from app.extensions import generate_token

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET"])
def register():
    return success("nihao ", msg="注册成功")


@auth_bp.route("/login", methods=["GET"])
def login():
    return success(data="登录成功"
    , msg="登录成功")