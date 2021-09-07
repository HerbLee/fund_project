import random
import string
import hashlib
import uuid


def random_string(length=8, letters=None):
    if letters is None:
        # 大小写加字母加数字
        letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def uid():
    return str(uuid.uuid4()).replace("-", "")


def sha256_hash(s, salt=''):
    return hashlib.sha256((s + salt).encode()).hexdigest()


if __name__ == '__main__':
    print(uid())
    print(len(uid()))
