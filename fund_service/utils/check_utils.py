"""
check args
"""
import re


def judge_phone(tel):
    tel = str(tel)
    ret = re.match(r"^1[35789]\d{9}$", tel)
    if ret:
        return True
    else:
        return False
