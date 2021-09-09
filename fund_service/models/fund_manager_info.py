import sqlalchemy as sa
from sqlalchemy.dialects.mysql import INTEGER, DECIMAL, TINYINT
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime

FundManagerInfoModel = sa.Table(
    'fund_manager_info', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('create_time', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_time', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('is_delete', TINYINT(1), nullable=False, comment='删除状态0 未删除1已删除', default=0),
    sa.Column('info_id', sa.Integer, nullable=False, comment='基金ID'),
    sa.Column('manager_id', sa.Integer, nullable=False, comment='基金经理ID'),
    sa.Index('idx_fund_manager_info_infoid', 'info_id', unique=True),
    sa.Index('idx_manager_info_maid', 'manager_id', unique=True),
    comment='基金信息和基金经理关联表'
)


class FundCompanyInfoSchema(Schema):
    id = fields.Integer()
    # company_name = fields.String()
    # company_code = fields.Integer()
    # info = fields.String()
    # createUser = fields.Integer(attribute='create_user')
    # avatarId = fields.Integer(attribute='avatar_id', allow_none=True)
