import random
import string

ALPHANUMERIC = string.ascii_lowercase + string.digits
STRING_LEN = 6


def gen_random_string(chars=ALPHANUMERIC, length=STRING_LEN):
    return ''.join(random.choice(chars) for _ in range(length))
