import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER, DECIMAL, TINYINT
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime,LocalDate

FundManagerModel = sa.Table(
    'fund_manager', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('create_time', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_time', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('is_delete', TINYINT(1), nullable=False, comment='删除状态0 未删除1已删除', default=0),
    sa.Column('name', sa.VARCHAR(10), nullable=False, comment='姓名'),
    sa.Column('education', TINYINT(1), nullable=False, comment='学历 0大专 1本科 2 硕士 3 博士', default=0),
    sa.Column('b_date', LocalDate, nullable=False, comment='任职日期'),
    sa.Column('rh_date', LocalDate, nullable=False, comment='入行日期'),
    sa.Column('resume', sa.VARCHAR(900), comment='简历'),
    sa.Column('nav_rate', DECIMAL(8, 4), nullable=False, comment='任期回报率', default=0.0000),
    sa.Column('hy_nav_rate', DECIMAL(8, 4), nullable=False, comment='同类平均回报', default=0.0000),
    sa.Index('idx_fund_manager_name', 'name', unique=True),
    comment='基金经理表'
)


class FundManagerSchema(Schema):
    id = fields.Integer()
    company_name = fields.String()
    company_code = fields.Integer()
    # info = fields.String()
    # createUser = fields.Integer(attribute='create_user')
    # avatarId = fields.Integer(attribute='avatar_id', allow_none=True)
