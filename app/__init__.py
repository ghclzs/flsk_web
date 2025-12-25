from flask import Flask
from app.config import config
from app.extensions import db, migrate
from app.blueprints import register_blueprints
from app.utils.response import success


def create_app(config_name=None):
    """应用工厂函数"""
    if not config_name:
        config_name = "default"

    app = Flask(__name__)
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





