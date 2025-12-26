import logging
import os
from logging.handlers import RotatingFileHandler

from app.config import config
from app.extensions import db, migrate
from app.blueprints import register_blueprints
from app.utils.response import success
from flask import Flask, request, jsonify, g
import time
import uuid

def create_app(config_name=None):
    """应用工厂函数"""
    if not config_name:
        config_name = "default"

    app = Flask(__name__)
    # ========== 1. 基础日志配置 ==========
    # 设置日志级别（DEBUG 会输出所有级别日志，生产环境建议设为 INFO/WARNING）
    app.logger.setLevel(logging.DEBUG)

    # 避免重复添加处理器（多次启动时）
    if not app.logger.handlers:
        # ========== 2. 配置控制台输出 ==========
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # 控制台输出 DEBUG 及以上级别

        # ========== 3. 配置文件输出（按大小分割，避免日志文件过大） ==========
        # 创建日志目录（不存在则创建）
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
        os.makedirs(log_dir, exist_ok=True)
        # 日志文件路径
        log_file = os.path.join(log_dir, "flask_app.log")
        # 配置文件处理器：单个文件最大 10MB，保留 5 个备份
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8"  # 避免中文乱码
        )
        file_handler.setLevel(logging.INFO)  # 文件只记录 INFO 及以上级别

        # ========== 4. 配置日志格式（包含时间、级别、模块、内容） ==========
        log_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(log_formatter)
        file_handler.setFormatter(log_formatter)

        # ========== 5. 添加处理器到 Flask logger ==========
        app.logger.addHandler(console_handler)
        app.logger.addHandler(file_handler)

    # 测试日志输出
    app.logger.debug("Flask 应用初始化完成（调试信息）")
    app.logger.info("Flask 应用启动成功（普通信息）")

    # 加载配置
    app.config.from_object(config[config_name])

    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)

    # 4. 关键：导入模型（必须在db.init_app之后）
    # 让db识别模型，否则迁移工具无法生成表
    with app.app_context():
        from app.models import student  # 导入所有模型文件

    # 注册蓝图
    register_blueprints(app)

    # 测试路由（根路径）
    @app.route("/")
    def index():
        return success(msg="Flask Web项目启动成功！")

    return app





