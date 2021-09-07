from models import UserModel
from utils.string_utils import random_string, sha256_hash
import sqlalchemy.sql as sasql


class UserService(object):
    """
    user service
    """

    def __init__(self, request):
        self.config = request.app.config
        self.cache = request.app.cache
        self.db = request.app.db

    async def create(self, **data):
        """
        创建用户
        :param data:
        :return:
        """
        data['salt'] = random_string(64)
        data['password'] = sha256_hash(data['password'], data['salt'])
        data['username'] = "".join(['nickname', str(data['mobile'])])
        data['name'] = "".join(['nickname', str(data['mobile'])])

        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(UserModel).values(**data))
            id = result.lastrowid

        return await self.info(id)

    async def existence_mobile(self, mobile):
        """
        判断手机号是否已经存在
        :param mobile:
        :return:
        """
        if await self.info_by_mobile(mobile) is not None:
            return True
        return False

    async def edit(self, id, **data):
        """
        修改用户信息
        :param id:
        :param data:
        :return:
        """
        data = {k: v for k, v in data.items() if v is not None}
        if 'password' in data:
            user = self.info(id)
            data['password'] = sha256_hash(data['password'], user['salt'])

        async with self.db.acquire() as conn:
            await conn.execute(sasql.update(UserModel).where(UserModel.c.id == id).values(**data))

        return await self.info(id)

    async def info(self, id):
        """
        获取用户信息
        :param id: 用户id
        :return:
        """
        async with self.db.acquire() as conn:
            result = await conn.execute(UserModel.select().where(UserModel.c.id == id))
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_username(self, username):
        """
        根据username获取对象
        :param username: 用户名
        :return:
        """

        async with self.db.acquire() as conn:
            result = await conn.execute(UserModel.select().where(UserModel.c.username == username))
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_name(self, name):
        """
        name
        :param name: 用户名
        :return:
        """

        async with self.db.acquire() as conn:
            result = await conn.execute(UserModel.select().where(UserModel.c.name == name))
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_mobile(self, mobile):
        """
        根据mobile查询对象
        :param mobile:
        :return:
        """

        async with self.db.acquire() as conn:
            result = await conn.execute(UserModel.select().where(UserModel.c.mobile == mobile))
            row = await result.first()

        return None if row is None else dict(row)

    async def infos(self, ids):
        """
        获取多个用户信息
        :param ids:
        :return:
        """
        async with self.db.acquire() as conn:
            result = await conn.execute(UserModel.select().where(UserModel.c.id.in_(ids)))

            d = {v['id']: dict(v) for v in await result.fetchall()}

        return [d[v] for v in ids]

    async def list_(self, *, limit=None, offset=None):
        """
        获取列表数据
        :param limit:
        :param offset:
        :return:
        """
        async with self.db.acquire() as conn:
            select_sm = UserModel.select()
            count_sm = sasql.select([sasql.func.count()]).select_from(UserModel)

            select_sm.order_by(UserModel.c.created_at.desc())

            if limit is not None:
                select_sm = select_sm.limit(limit)
            if offset is not None:
                select_sm = select_sm.offset(offset)

            result = await conn.execute(select_sm)
            rows = [dict(v) for v in await result.fetchall()]

            result = await conn.execute(count_sm)
            total = await result.scalar()

        return (rows, total)
