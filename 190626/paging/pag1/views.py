from django.shortcuts import render, HttpResponse
from pag1 import page

# 自动生成一个列表
# LIST = []
# for i in range(500):
#     LIST.append(i)
#
#
# def user_list(request):
#     page_obj = page.Paginator(100, 1, 'http://127.0.0.1:8000/user_list/')
#     return render(request, 'user_list.html', {'page_obj': page_obj})

#
# total_item_count: 总记录数
#         :param current_page:  当前页码
#         :param base_url: 页码的前缀URL


LIST = []
for i in range(500):
    LIST.append(i)


def user_list(request):
    current_page = int(request.GET.get('p', 1))

    page_obj = page.Paginator(len(LIST), current_page, "/user_list/")
    return render(request, 'user_list.html', {'page_obj': page_obj})
