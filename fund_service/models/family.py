import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime

FamilyModel = sa.Table(
    'family', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('created_ts', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_ts', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('uuid', sa.VARCHAR(32), nullable=False, comment='uuid'),
    sa.Column('name', sa.VARCHAR(64), nullable=False, comment='家庭名称'),
    sa.Column('info', sa.VARCHAR(255), nullable=True, comment='家庭信息'),
    sa.Column('avatar_id', sa.Integer, nullable=True, comment='头像'),
    sa.Column('create_user', None, sa.ForeignKey("user.id"), comment='创建人'),
    sa.Index('idx_family_name', 'name', unique=True),
    sa.Index('idx_family_uuid', 'uuid', unique=True),
    comment='家庭表'
)


class FamilySchema(Schema):
    id = fields.Integer()
    uuid = fields.String()
    name = fields.String()
    info = fields.String()
    createUser = fields.Integer(attribute='create_user')
    avatarId = fields.Integer(attribute='avatar_id', allow_none=True)


