import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from models.common import metadata, LocalDateTime

UserModel = sa.Table(
    'user', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('created_ts', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='create time'),
    sa.Column('update_ts', LocalDateTime, nullable=False, server_default=sasql.text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='update time'),
    sa.Column('username', sa.VARCHAR(20), nullable=True, comment='用户名'),
    sa.Column('name', sa.VARCHAR(20), nullable=True, comment='姓名'),
    sa.Column('password', sa.CHAR(64), nullable=False, comment='密码'),
    sa.Column('salt', sa.CHAR(64), nullable=False, comment='密钥'),
    sa.Column('mobile', sa.VARCHAR(11), nullable=False, comment='手机号'),
    sa.Column('gender', sa.CHAR(1), nullable=True, comment='性别'),
    sa.Column('birthday', sa.Date, nullable=True, comment='出生年月日'),
    sa.Column('intro', sa.VARCHAR(100), server_default='', nullable=False, comment='自我介绍'),
    sa.Column('avatar_id', sa.Integer, nullable=True, comment='头像'),
    sa.Index('idx_username', 'username', unique=True),
    sa.Index('idx_mobile', 'mobile', unique=True),
    comment='用户表'
)


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String(allow_none=True)
    name = fields.String(allow_none=True)
    mobile = fields.String()
    gender = fields.Integer(allow_none=True)
    birthday = fields.Date(format="%Y-%m-%d", allow_none=True)
    intro = fields.String(allow_none=True)
    avatarId = fields.Integer(attribute='avatar_id', allow_none=True)


