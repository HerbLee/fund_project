from sanic import Blueprint
from .account import account
from .family import family


api = Blueprint.group(account, family, url_prefix="/api")
