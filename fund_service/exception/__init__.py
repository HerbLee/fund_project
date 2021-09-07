from enum import Enum
from .common_execption import MissingArgumentException, BadParameterException, NoPermission


class CommonExceptionCode(Enum):
    MISSING_ARGUMENT = 10001
    ARGUMENT_TYPE_ERROR = 10002 # 类型错误,比如json 或者表单
    BAD_PARAMETER_ERROR = 10003 # 参数格式错误
