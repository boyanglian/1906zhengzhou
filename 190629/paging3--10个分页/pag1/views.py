from django.shortcuts import render
from utils.pager import Pagination  # 导入分页模型类 Pagination
from pag1 import models


def host(request):
    # 统计出一共有多少条 数据
    all_count = models.Host.objects.all().count()

    #                                   current_page, total_count, base_url,
    # page_obj = Pagination 方法需要 3个 参数(请求当前页码，总数据条数，该应用路径)
    page_obj = Pagination(request.GET.get('page'), all_count, request.path_info)

    # host_list = models.Host.objects.all()[本页内容的开始,本页内容的结束]
    # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    host_list = models.Host.objects.all()[page_obj.start:page_obj.end]

    # render(request, 页面, {展示内容，展示的 html页码})
    return render(request, 'host.html', {'host_list': host_list, 'page_html': page_obj.page_html()})

# 简版
# def host(request):
#     host_obj = models.Host.objects.all()
#     all_count = host_obj.count()
#     page_obj = Pagination(request.GET.get('page'), all_count, request.path_info)
#     host_list = host_obj[page_obj.start:page_obj.end]
#     return render(request, 'host.html', {'host_list': host_list, 'page_html': page_obj.page_html()})
