from sanic import Blueprint
from .account import account
from .family import family
from .fund_company import company


api = Blueprint.group(company, url_prefix="/api")
