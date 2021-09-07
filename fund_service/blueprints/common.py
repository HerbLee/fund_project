from enum import Enum
from sanic import response
from sanic.exceptions import SanicException, InvalidUsage, NotFound
from services import ServiceException
from exception import CommonExceptionCode, MissingArgumentException, BadParameterException, NoPermission
import traceback
from functools import wraps
from utils.const_utils import RedisCode
import json
from models import UserSchema


class ResponseCode(Enum):
    OK = 0
    FAIL = 1


def response_json(code=ResponseCode.OK, message='', status=200, **data):
    return response.json({
        'code': code.value,
        'message': message,
        'data': data
    }, status)


def authenticated():
    """
    装饰器
    :return:
    """
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            token = request.headers.get('haven-token')
            if token is None:
                raise MissingArgumentException('haven-token is None')
            user = await request.app.cache.get("_".join([RedisCode.USER_TOKEN.value, token]))
            if user is None:
                raise NoPermission('No permission please login')
            user = UserSchema().loads(user)
            # 重置token时间
            await request.app.cache.expire("_".join([RedisCode.USER_TOKEN.value, token]),
                                           request.app.config['USER_TOKEN_EXPIRE'])

            return await f(request, user, *args, ** kwargs)

        return decorated_function
    return decorator


def handle_exception(request, e):
    code = ResponseCode.FAIL
    message = repr(e)
    status = 500
    data = {}

    if isinstance(e, InvalidUsage):
        message = e.message
        if e.code is not None:
            code = e.code
        status = 200
        data['error_code'] = CommonExceptionCode.ARGUMENT_TYPE_ERROR.value
    elif isinstance(e, NotFound):
        message = e.args[0]
        status = 200

    elif isinstance(e, NoPermission):
        message = e.message
        if e.code is not None:
            code = e.code
        status = 403
    elif isinstance(e, SanicException):
        status = e.status_code
    elif isinstance(e, ServiceException):
        message = e.message
        if e.code is not None:
            code = e.code
        status = 200

    elif isinstance(e, MissingArgumentException):
        message = e.message
        if e.code is not None:
            code = e.code
        status = 200
        data['error_code'] = CommonExceptionCode.MISSING_ARGUMENT.value
    elif isinstance(e, BadParameterException):
        message = e.message
        if e.code is not None:
            code = e.code
        status = 200
        data['error_code'] = CommonExceptionCode.BAD_PARAMETER_ERROR.value

    # if request.app.config['DEBUG']:
    #     data['exception'] = traceback.format_exc()

    return response_json(code, message, status, **data)
