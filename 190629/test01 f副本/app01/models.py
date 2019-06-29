from django.db import models
from django.utils import datetime_safe


class MyField(models.Field):
    description = '自定义一个char字段'

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        kwargs['max_length'] = max_length
        # 初始化父类方法
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        # 自定义类型跟数据库字段类型对应
        return "char(%s)" % self.max_length


# Create your models here.
#  models.Model 系统模型，自定义模型继承了它，拥有了该模型的所有方法
# 出版社表
class Press(models.Model):
    id = models.AutoField(primary_key=True)
    press_name = models.CharField(max_length=35, null=False, unique=True)

    def __str__(self):
        # 当对象被作为字符串打印时，会自动调用
        # return "<press: press_name-{}>" % (self.press_name,)
        return "<press: press_name-{}>".format(self.press_name)

    class Meta:
        ordering = ['id']


# 书模型
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    books_name = models.CharField(max_length=25, null=False)
    press = models.ForeignKey(to="Press", related_name="pb", on_delete=models.DO_NOTHING, null=True, default=1)

    publish_date = models.DateField(auto_now=datetime_safe.date)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    stock = models.PositiveSmallIntegerField(default=50)
    sales_num = models.PositiveIntegerField(default=0)
    us_shelf = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']


# 作者模型
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35, null=False)
    # 作者和书表建立多对多的关系
    bookss = models.ManyToManyField(Books)
    # 邮箱
    email = models.EmailField(max_length=50, default='')  # varchar(50)
    # 身份证
    number_id = MyField(18)
