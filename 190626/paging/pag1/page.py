from django.utils.safestring import mark_safe

class Paginator:
    '''
    页码的格式依赖于bootstrap；
    使用案例：
    from django.shortcuts import render,redirect,HttpResponse
    from app01.models import *
    from tools import page  导入
    def index(request):
        base_url = request.path_info
        total_item_count = UserInfo.objects.all().count()
        current_page = int(request.GET.get('page',1))
        page_obj = page.Paginator(total_item_count,current_page,base_url)
        user_list = UserInfo.objects.all()[page_obj.start:page_obj.end]
        return render(request,'index.html',{'user_list':user_list,'html_page': page_obj.pager})
    '''
    def __init__(self,total_item_count,current_page,base_url,per_page_item_count=10,show_pager_count=11):
        '''
        :param total_item_count: 总记录数
        :param current_page:  当前页码
        :param base_url: 页码的前缀URL
        :param per_page_item_count: 每页显示的记录数
        :param show_pager_count: 显示的页码个数
        '''

        self.total_item_count = total_item_count
        self.current_page = current_page
        self.base_url = base_url
        self.per_page_item_count = per_page_item_count
        self.show_pager_count = show_pager_count

        total_page, res = divmod(self.total_item_count, self.per_page_item_count)
        if res:
            total_page += 1

        self.total_page = total_page
        self.half_show_pager_count = int(total_page/2)

    @property
    def start(self):
        '''
        页码查询数据的开始位置
        :return:
        '''
        return (self.current_page-1)*self.per_page_item_count

    @property
    def end(self):
        '''
        页码查询数据的结束位置
        :return:
        '''
        return self.current_page*self.per_page_item_count

    @property
    def pager(self):
        '''
        返回需要的前端页码
        :return:
        '''
        page_list = []
        ul = ' <ul class="pagination">'
        page_list.append(ul)

        if self.current_page == 1:
            prev = ' <li><a href="#">上一页</a></li>'
        else:
            prev = ' <li><a href="%s?page=%s">上一页</a></li>' % (self.base_url, self.current_page - 1)

        page_list.append(prev)

        # 如果数据特别少：
        if self.total_page < self.show_pager_count:
            pager_start = 1
            pager_end = self.total_page + 1

        else:
            if self.current_page <= self.half_show_pager_count:
                pager_start = 1
                pager_end = self.show_pager_count + 1

            else:
                if self.current_page + self.half_show_pager_count > self.total_page:
                    pager_start = self.total_page - self.show_pager_count + 1
                    pager_end = self.total_page + 1
                else:
                    pager_start = self.current_page - self.half_show_pager_count
                    pager_end = self.current_page + self.half_show_pager_count + 1

        for i in range(pager_start, pager_end):
            if i == self.current_page:
                tpl = ' <li class="active"><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i,)
            else:
                tpl = ' <li><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i,)
            page_list.append(tpl)

        if self.current_page == self.total_page:
            nex = ' <li><a href="#">下一页</a></li>'
        else:
            nex = ' <li><a href="%s?page=%s">下一页</a></li>' % (self.base_url, self.current_page + 1,)

        page_list.append(nex)

        lu = ' </ul>'
        page_list.append(lu)

        html_page = mark_safe(''.join(page_list))
        return html_page

