import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER, DECIMAL
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime

FundCompanyModel = sa.Table(
    'fund_company', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('create_time', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_time', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('company_name', sa.VARCHAR(64), nullable=False, comment='公司名称'),
    sa.Column('company_code', INTEGER(display_width=8, unsigned=True, zerofill=True), nullable=False, comment='公司代码'),
    sa.Column('of_num', INTEGER(4), nullable=False, comment='开放基金数', default=0),
    sa.Column('cf_num', INTEGER(4), nullable=False, comment='封闭基金数', default=0),
    sa.Column('total_num', INTEGER(4), nullable=False, comment='总基金数', default=0),
    sa.Column('share_open', DECIMAL(8, 2), nullable=False, comment='开放基金份额', default=0.00),
    sa.Column('share_close', DECIMAL(8, 2), nullable=False, comment='封闭基金份额', default=0.00),
    sa.Column('share_total', DECIMAL(8, 2), nullable=False, comment='总基金份额', default=0.00),
    sa.Index('idx_fund_company_name', 'company_name', unique=True),
    sa.Index('idx_company_code', 'company_code', unique=True),
    comment='基金公司表'
)


class FundCompanySchema(Schema):
    id = fields.Integer()
    company_name = fields.String()
    company_code = fields.Integer()
    # info = fields.String()
    # createUser = fields.Integer(attribute='create_user')
    # avatarId = fields.Integer(attribute='avatar_id', allow_none=True)
