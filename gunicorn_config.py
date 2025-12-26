# /www/flask_app/gunicorn_config.py （若需要迁移配置文件位置，可改为 /opt/gh_java/flsk_web/gunicorn_config.py）
import multiprocessing
import os

# ===================== 核心路径修正 =====================
# 项目根路径（你的实际路径）
PROJECT_ROOT = "/opt/gh_java/flsk_web"
# 确保日志目录存在（Python语法实现，替代终端mkdir命令）
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

# ===================== 服务配置 =====================
# 绑定内网端口（仅 Nginx 访问）
bind = "127.0.0.1:8000"

# 工作进程数（CPU核心数*2+1）
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class = "sync"

# ===================== 日志配置（修正路径） =====================
accesslog = os.path.join(LOG_DIR, "access.log")  # 访问日志
errorlog = os.path.join(LOG_DIR, "error.log")    # 错误日志
loglevel = "info"                                # 日志级别：debug/info/warning/error/critical

# ===================== 其他配置（修正路径） =====================
pidfile = os.path.join(PROJECT_ROOT, "gunicorn.pid")  # PID文件路径
timeout = 60                                          # 请求超时时间
keepalive = 5                                         # 长连接保持时间
daemon = True                                         # 后台运行

# 全局 Python 路径（关键：指定系统 Python3 解释器，若用虚拟环境需改为虚拟环境的python路径）
pythonpath = "/usr/bin/python3"

# 可选：若项目有虚拟环境，指定虚拟环境的Python解释器（示例）
# pythonpath = "/opt/gh_java/flsk_web/venv/bin/python3"