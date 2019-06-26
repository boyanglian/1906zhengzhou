import os
import sys
import random

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paging2.settings')
    import django

    django.setup()

    from pag1.models import *

    # 查询测试
    # books = [
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    #     {'books_name':'大地啊', 'publish_date': '2019-06-25 13:30', 'price': 20, "stock": 100, 'sales_num': 10, 'us_shelf': 1},
    # ]
    # for book in books:
    #     Books.objects.create(**book)
    #     # Books.objects.create(books_name='大地啊', publish_date='2019-06-25 13:30')

    # books = Books.objects.values('id', 'books_name', 'stock', 'sales_num')[10:20]
    # print(books)

    # 生成测试数据
    # lists = [Host(press_name="乌龙闯关记第{}关".format(i))
    #          for i in range(0, 400)]
    # # print(lists)
    # # 分块 批量添加数据
    # Host.objects.bulk_create(lists, 10)
