from django.shortcuts import render

# Create your views here.
# 导入 通过 Pagination 封装的 分页功能 包
from utils.pager import Pagination
from pag1 import models

def host(request):
    # 统计出一共有多少条 数据
    all_count = models.Host.objects.all().count()
    # page_obj = Pagination 方法需要 3个 参数(请求当前页码，总数据条数，该应用路径)
    # page_obj = Pagination(request.GET.get('page'),all_count,'/host/')
    page_obj = Pagination(request.GET.get('page'),all_count,request.path_info)

    # host_list = models.Host.objects.all()[本页内容的开始,本页内容的结束]
    host_list = models.Host.objects.all()[page_obj.start:page_obj.end]
    print(models.Host.objects.all()[0:5])

    # render(request, 页面, {展示内容，展示的 html页码})
    return render(request, 'host.html', {'host_list': host_list, 'page_html': page_obj.page_html()})
