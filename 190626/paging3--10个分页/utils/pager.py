# mark_safe 是将 html 格式代码传到 前端时，在页面可以直接渲染
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, current_page, total_count, base_url, per_page_count=20, max_pager_num=10):
        """
        :param current_page: 用户请求的当前页
        :param total_count:  数据库中查询到的数据总条数
        :param base_url:    请求的 url 路径
        :param per_page_count: 每页显示的数据条数
        :param max_pager_num: 页面上最多显示的页码
        """
        # url 地址  “/host/”
        self.base_url = base_url

        # divmod(total_count, per_page_count)  总条数/每页显示条数   得到得 (商,余) 赋值给 total_page_count总页数, div余值
        total_page_count, div = divmod(total_count, per_page_count)
        if div:
            # 如果 div 有值 总页数 +1
            total_page_count += 1
        # total_page_count 总页数
        self.total_page_count = total_page_count

        # 判断当前 获取 得页码值
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1

        # 如果当前页，大于 总页数，当前页 = 总页数
        if current_page > total_page_count:
            current_page = total_page_count

        self.current_page = current_page
        self.per_page_count = per_page_count
        self.total_count = total_count
        self.max_pager_num = max_pager_num
        # 当前页前后 几个  页码
        self.half_max_pager_num = int(max_pager_num / 2)

    @property
    def start(self):
        # 开始显示id 值 为 (当前页-1)*每页显示条数
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        # 结束显示id 值 为 当前页*每页显示条数
        return self.current_page * self.per_page_count

    # html 具体显示内容
    def page_html(self):
        page_html_list = []

        # 首页
        head_page = "<li><a href='%s?page=%s'>首页</a></li>" % (self.base_url, 1)
        page_html_list.append(head_page)

        if self.current_page <= 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='%s?page=%s'>上一页</a></li>" % (self.base_url, self.current_page - 1,)
        page_html_list.append(prev)

        max_pager_num = self.max_pager_num
        half_max_pager_num = int(max_pager_num // 2)

        # 数据总页数 < 页面上最大显示的页码个数
        if self.total_page_count <= max_pager_num:
            page_start = 1
            page_end = self.total_page_count
        else:
            # 数据比较多，已经超过11个页码
            # 如果当前页 <=5,显示 1-11
            if self.current_page <= half_max_pager_num:
                page_start = 1
                page_end = max_pager_num
            else:
                # 当前页 >=6
                if (self.current_page + half_max_pager_num) > self.total_page_count:
                    page_end = self.total_page_count
                    # page_start = current_page - 5
                    page_start = self.total_page_count - max_pager_num
                else:
                    page_start = self.current_page - half_max_pager_num  # 当前页 - 5
                    page_end = self.current_page + half_max_pager_num - 1  # 当前页 + 5

        for i in range(page_start, page_end + 1):
            if self.current_page == i:
                tag = "<li><a class='active' href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            else:
                tag = "<li><a href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            page_html_list.append(tag)

        # 下一页
        if self.current_page >= self.total_page_count:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='%s?page=%s'>下一页</a><li>" % (self.base_url, self.current_page + 1,)
        page_html_list.append(nex)

        # 尾页
        tail_page = "<li><a href='%s?page=%s'>尾页</a></li>" % (self.base_url, self.total_page_count)
        page_html_list.append(tail_page)

        # 将拼接的页码数据 join 序列化 传到 模板
        # print("".join(page_html_list))
        return mark_safe("".join(page_html_list))