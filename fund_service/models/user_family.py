import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime

UserFamilyModel = sa.Table(
    'user_family', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('created_ts', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_ts', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('user_id', sa.Integer, nullable=False),
    sa.Column('family_uuid', sa.VARCHAR(32), nullable=False),
    sa.Column('create_user', sa.Integer, nullable=False),
    sa.Column('roles', sa.Integer, nullable=False, comment='角色 0 创建者, 1 普通成员'),
    sa.Index('idx_user_family_user_id', 'user_id', 'family_uuid', unique=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE', onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['family_uuid'], ['family.uuid'], ondelete='CASCADE', onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['create_user'],['user.id'], ondelete='CASCADE',onupdate='CASCADE'),
    comment='家庭用户表'
)


class UserFamilySchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    roles = fields.Integer()
    family_uid = fields.String()
    createUser = fields.Integer(attribute='create_user')
