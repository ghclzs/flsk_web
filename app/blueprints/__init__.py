# from app.blueprints.auth.routes import auth_bp
from app.blueprints.code.routes import code_bp
from app.blueprints.student.routes import student_bp
# from app.blueprints.user.routes import user_bp

# 统一注册所有蓝图
def register_blueprints(app):
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(user_bp)
    app.register_blueprint(code_bp)
    app.register_blueprint(student_bp)