from models import FamilyModel, UserFamilyModel
import sqlalchemy.sql as sasql
from utils import string_utils


class FamilyService(object):
    """
    family service
    """

    def __init__(self, request):
        self.config = request.app.config
        self.cache = request.app.cache
        self.db = request.app.db

    async def create(self, **data):
        """
        创建家庭
        :param data:
        :return:
        """
        uuid = string_utils.uid()
        data['uuid'] = uuid
        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(FamilyModel).values(**data))
            id = result.lastrowid
            data.pop('info')
            data.pop('name')
            data.pop('uuid')
            data['user_id'] = data['create_user']
            data['family_uuid'] = uuid
            data['roles'] = 0
            await conn.execute(sasql.insert(UserFamilyModel).values(**data))
        return await self.info(id)


    async def edit(self, uuid, **data):
        """
        修改用户信息
        :param id:
        :param data:
        :return:
        """
        data = {k: v for k, v in data.items() if v is not None}

        async with self.db.acquire() as conn:
            await conn.execute(sasql.update(FamilyModel).where(FamilyModel.c.uuid == uuid).values(**data))
        # 这里要改
        return await self.info_by_uuid(uuid)


    async def info(self, id):
        """
        获取用户信息
        :param id: 用户id
        :return:
        """
        async with self.db.acquire() as conn:
            result = await conn.execute(FamilyModel.select().where(FamilyModel.c.id == id))
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_uuid(self, uuid):
        """
        获取用户信息
        :param uuid: 用户uuid
        :return:
        """
        async with self.db.acquire() as conn:
            result = await conn.execute(FamilyModel.select().where(FamilyModel.c.uuid == uuid))
            row = await result.first()

        return None if row is None else dict(row)