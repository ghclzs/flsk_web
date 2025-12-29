from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# 初始化数据库
db = SQLAlchemy()
migrate = Migrate()
cors = CORS(supports_credentials=True)  # 支持凭据，允许跨域访问

# def init_extensions(app):
#     db.init_app(app)  # 将数据库连接绑定到Flask app
#     migrate.init_app(app, db)
