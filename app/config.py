import os
from dotenv import load_dotenv

# 加载环境变量
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config:
    """基础配置"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭不必要的警告
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭不必要的警告
    SQLALCHEMY_ENGINE_OPTIONS = {  # 连接池配置（可选）
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True  # 检查连接有效性
    }

if __name__ == '__main__':
    print(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False


# 配置映射
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}