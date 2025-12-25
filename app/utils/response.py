from flask import jsonify

def success(data=None, msg="操作成功"):
    """成功响应"""
    return jsonify({
        "code": 200,
        "msg": msg,
        "data": data
    })

def fail(msg="操作失败", code=400):
    """失败响应"""
    return jsonify({
        "code": code,
        "msg": msg,
        "data": None
    })