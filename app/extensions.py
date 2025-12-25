from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 初始化数据库
db = SQLAlchemy()
migrate = Migrate()


def init_extensions(app):
    db.init_app(app)  # 将数据库连接绑定到Flask app
    migrate.init_app(app, db)
