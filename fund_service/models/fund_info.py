import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER, DECIMAL, TINYINT
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime,LocalDate

FundInfoModel = sa.Table(
    'fund_info', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('create_time', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_time', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('is_delete', TINYINT(1), nullable=False, comment='删除状态0 未删除1已删除', default=0),
    sa.Column('fund_name', sa.VARCHAR(32), nullable=False, comment='基金名称'),
    sa.Column('fund_simple_name', sa.VARCHAR(16), nullable=False, comment='基金简称'),
    sa.Column('fund_code', INTEGER(display_width=6, unsigned=True, zerofill=True), nullable=False, comment='基金代码'),
    sa.Column('found_date', LocalDate, nullable=False, comment='创立日期'),
    sa.Column('operation_mode', TINYINT(1), nullable=False, comment='运作方式 0开放式', default=0),
    sa.Column('category', TINYINT(1), nullable=False, comment='基金类型', default=0),
    sa.Column('sub_category', TINYINT(2), nullable=False, comment='二级分类', default=0),
    sa.Index('idx_fund_info_name', 'fund_simple_name', unique=True),
    sa.Index('idx_fund_info_code', 'fund_code', unique=True),
    comment='基金信息表'
)


class FundInfoSchema(Schema):
    id = fields.Integer()
    company_name = fields.String()
    company_code = fields.Integer()
    # info = fields.String()
    # createUser = fields.Integer(attribute='create_user')
    # avatarId = fields.Integer(attribute='avatar_id', allow_none=True)
