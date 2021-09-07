from sanic import Blueprint
from services import FamilyService
from blueprints.common import response_json, ResponseCode, authenticated
from models import FamilySchema
from utils.string_utils import sha256_hash, random_string
from exception import MissingArgumentException, BadParameterException
from utils import check_utils, RedisCode, DateEncoder, datetime_utils
import json
import datetime

family = Blueprint("family", url_prefix='/family', version=1)



@family.post("/create")
@authenticated()
async def create(request, user):
    data = request.form

    name = data.get('name')
    info = data.get('info')

    if name is None or info is None:
        raise MissingArgumentException('name or info is None')

    family_service = FamilyService(request)

    family = await family_service.create(name=name, info=info, create_user=user.get('id'))

    return response_json(family=FamilySchema().dump(family))

#
# @account.post("/login")
# async def login(request):
#     data = request.form
#     mobile = data.get("mobile")
#     password = data.get("password")
#
#     if mobile is None:
#         raise MissingArgumentException('please input mobile')
#     if password is None:
#         raise MissingArgumentException('please input password')
#     if not check_utils.judge_phone(mobile):
#         raise BadParameterException('mobile type error')
#
#     user_service = UserService(request)
#     user = await user_service.info_by_mobile(mobile)
#
#     if user is not None and sha256_hash(password, user['salt']) == user['password']:
#         # save to redis
#         token = random_string(32)
#         redis_key = "_".join([RedisCode.USER_TOKEN.value, str(user.get("id"))])
#         pre_token = await request.app.cache.get(redis_key)
#         # 如果该用户下已有token ,清除上次的 token
#         if pre_token is not None:
#             await request.app.cache.delete("_".join([RedisCode.USER_TOKEN.value, str(pre_token, encoding="utf-8")]))
#         await request.app.cache.set(redis_key, token)
#         await request.app.cache.set("_".join([RedisCode.USER_TOKEN.value, token]), UserSchema().dumps(user))
#         # 设置过期时间为1天
#         await request.app.cache.expire("_".join([RedisCode.USER_TOKEN.value, token]),
#                                        request.app.config['USER_TOKEN_EXPIRE'])
#
#         return response_json(message='login success', token=token)
#     else:
#         return response_json(ResponseCode.FAIL, 'mobile or password error')
#
#
# @account.get("/info")
# @authenticated()
# async def get_user(request, user):
#     return response_json(message="get user info success", user=UserSchema().dump(user))
#
#
# @account.post("/update")
# @authenticated()
# async def update_user(request, user):
#     """
#     修改用户信息 本接口只能修改 名字, 昵称, 性别, 自我介绍, 生日
#     :param request: 服务传递内容
#     :param user: 用户信息
#     :return:
#     """
#     request_data = request.form
#     token = request.headers.get('haven-token')
#     name = request_data.get('name')
#     username = request_data.get('username')
#     gender = request_data.get('gender')
#     intro = request_data.get('intro')
#     birthday = request_data.get('birthday')
#     update_params = {}
#     if name is not None and name != '' and name != user.get('name'):
#         update_params['name'] = name
#     if username is not None and username != '' and username != user.get('username'):
#         update_params['username'] = username
#     if gender is not None and gender != '' and gender != str(user.get('gender')):
#         update_params['gender'] = gender
#     if intro is not None and intro != '' and intro != user.get('intro'):
#         update_params['intro'] = intro
#     if birthday is not None and birthday != '' and datetime_utils.str_date(birthday) != user.get('birthday'):
#         update_params['birthday'] = datetime_utils.str_date(birthday)
#
#     if len(update_params) == 0:
#         return response_json(message='not update params', user=UserSchema().dump(user))
#     user_service = UserService(request)
#     resuser = await user_service.edit(user['id'], **update_params)
#     # 更新redis
#     await request.app.cache.set("_".join([RedisCode.USER_TOKEN.value, token]),
#                                 UserSchema().dumps(resuser))
#
#     return response_json(message="update user info success", user=UserSchema().dump(resuser))
