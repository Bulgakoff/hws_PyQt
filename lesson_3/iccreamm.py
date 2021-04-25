from datetime import datetime
from icecream import ic
import time

def plus_five(num):
    return num + 5

ic(plus_five(4))
ic(plus_five(5))

def hello(user:bool):
    if user:
        ic()
    else:
        ic()

hello(user=True)

# def time_format():
#     return f'{datetime.now()} ==> '
#
# ic.configureOutput(prefix=time_format)
#
# for _ in range(3):
#     time.sleep(1)
#     ic('qweqwe')


def plus_five(num):
    return num + 5

ic.configureOutput(includeContext=True)
ic(plus_five(4))
ic(plus_five(5))

def plus_five(num):
    return num + 5

ic(plus_five(4))
ic(plus_five(5))

for i in range(10):
    ic(f'****** Training model {i} ******')