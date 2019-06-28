# from functools import wraps

# def decorator(func):
#     @wraps(func)  # 修复装饰器
#     def inner(*args, **kwargs):
#         """
#         我是闭包函数
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         print('鹏祥')
#         func()
#         print('瑞磊')
#
#     return inner
#
# @decorator
# def test():
#     """
#     我是测试函数
#     :return:
#     """
#     print('淙琳')
#
#
# test()
#
# print(test.__name__, test.__doc__)

from functools import wraps


def decorator(func):               # 我是闭包函数
    @wraps(func)                   # 修复装饰器 # 无 鹏翔 淙琳 瑞磊 inner None
    def inner(*args, **kwargs):
        print('鹏翔')                          # 无 鹏翔 淙琳 瑞磊 test None
        func()
        print('瑞磊')

    return inner


@decorator
def test():                        # 我是测试函数
    print('淙琳')


test()
print(test.__name__, test.__doc__)
