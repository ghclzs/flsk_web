from datetime import datetime
from app.extensions import db  # 关联全局的db对象



# 定义 Model
class Api_test_report_results(db.Model):
    # 严格匹配数据库表名
    __tablename__ = "api_test_report_results"

    # 字段定义：完全匹配数据库的字段名和类型
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="主键ID（自增）"
    )
    project_name = db.Column(
        db.String(255),
        comment="项目名称"
    )
    # 注意：如果数据库中这些字段是数字类型（如 int），建议改用 Integer（更合理）
    # 若数据库中确实是 varchar，保留 String(255) 即可
    test_case_total = db.Column(
        db.Integer,  # 替换 String 为 Integer（数字类字段推荐）
        comment="测试用例总数"
    )
    test_passed_case_total = db.Column(
        db.Integer,
        comment="通过用例数"
    )
    test_failed_case_total = db.Column(
        db.Integer,
        comment="失败用例数"
    )
    test_skipped_case_total = db.Column(
        db.Integer,
        comment="跳过用例数"
    )
    # ========== 核心修正：字段名从 address → adress（少一个 d） ==========
    adress = db.Column(
        db.String(255),
        comment="地址"
    )
    all_adress = db.Column(
        db.String(255),
        comment="全部地址"
    )
    test_create_time = db.Column(
        db.TIMESTAMP,
        default=datetime.now,
        server_default=db.func.current_timestamp(),
        comment="创建时间"
    )

    # 模型转字典：同步修正字段名
    def to_dict(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "test_case_total": self.test_case_total,
            "test_passed_case_total": self.test_passed_case_total,
            "test_failed_case_total": self.test_failed_case_total,
            "test_skipped_case_total": self.test_skipped_case_total,
            # ========== 同步修正：address → adress ==========
            "adress": self.adress,
            "all_adress": self.all_adress,
            "test_create_time": self.test_create_time.strftime("%Y-%m-%d %H:%M:%S") if self.test_create_time else None
        }