from sanic import Blueprint
from blueprints.common import response_json, ResponseCode, authenticated
from utils.string_utils import sha256_hash, random_string
from exception import MissingArgumentException, BadParameterException
from utils import check_utils, RedisCode, DateEncoder, datetime_utils
import json
import datetime

company = Blueprint("company", url_prefix='/company', version=1)
from sanic_openapi import openapi


@company.post("/write_info")
# @openapi.parameter("code",str,description="基金代码")
@openapi.body("json", **{"name": {"type": int, "description": "名字"}})
async def write_info(request):
    """
    写入基金公司数据
    @Param: json 数据
    """

    return None


@company.post("/get_company_by_name")
async def get_company_by_name(request):
    """
    根据名字获取公司数据
    @Param: json 数据
    """

    return None
