from django.shortcuts import render,HttpResponse

from app01.models import *
from utils.page import Page
# Create your views here.

def index(request):
    # 获取当前页码
    try:
        page = int(request.GET.get('page', 1))
    except Exception as e:
        page = 1

    # 获取数据的总数
    book_count = Books.objects.count()
    # 书的总数 除以 每页显示的数
    page_count, m = divmod(book_count, 10)  # divmod 返回两个元素的元组， 第一个参数是商 第二个参数是余数
    if m:
        # 当余数不为空时 总页数加1
        page_count += 1

    # 实例化Page产生分页对象
    page = Page(page, page_count, '/app01/index/')
    print(page.start_pos, page.end_pos)
    # 根据开始和结束位置  获取数据
    books = Books.objects.values('id', 'books_name', 'stock', 'sales_num')[page.start_pos:page.end_pos]
    # 获取分页的html代码
    page_html = page.get_page_show()
    return render(request, 'books.html', {"books": books, 'page_html': page_html})
