from datetime import datetime, timedelta, timezone, date
import time

local_tz = timezone(timedelta(hours=8))


def as_local(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=local_tz)
    else:
        return dt.astimezone(local_tz)


def str_datetime(time_string, tp='%Y-%m-%d %H:%M:%S'):
    if time_string is None:
        return None
    return datetime.strptime(time_string, tp)


def str_mk_time(time_str, tp='%Y-%m-%d %H:%M:%S'):
    return time.mktime(str_datetime(time_str, tp))


def num_date(num):
    return date.fromtimestamp(num)

def str_date(st, tp='%Y-%m-%d'):
    return datetime.strptime(st, tp).date()