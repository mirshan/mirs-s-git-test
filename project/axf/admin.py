from django.contrib import admin
# Register your models here.
from .models import Wheel,Nav,Mustbuy,Foodtypes,Goods,User




#***********以下是按注册顺序显示列表***********
from django.contrib import admin
from django.utils.text import capfirst
# from django.utils.datastructures import OrderedDict


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner

admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
#**************结束******************

#注册轮播大图
@admin.register(Wheel)  #注册
class WheelsAdmin(admin.ModelAdmin):  # 类需要在需要的表里注册一下
    # 列表属性
    list_display = ['pk', 'img',  'name', 'trackid', 'isDelete']  # 显示列表的列
    list_filter = ['name','isDelete']  # 右侧增加过滤条件
    search_fields = ['name']  # 添加搜索框，按sname搜索,多加多条件
    list_per_page = 5  # 分页5条一分页

    # 添加、修改页属性
    fields = ['name',  'img', 'trackid','isDelete']  # 添加数据显示的顺序
    # fieldsets = []    不能与fields同时使用，二选一，是一个分组,元组

#注册产品分类导航
@admin.register(Nav)  #注册
class NavAdmin(admin.ModelAdmin):  # 类需要在需要的表里注册一下
    # 列表属性
    list_display = ['pk','img', 'name',  'trackid', 'isDelete']  # 显示列表的列
    list_filter = ['name','isDelete']  # 右侧增加过滤条件
    search_fields = ['name']  # 添加搜索框，按sname搜索,多加多条件
    list_per_page = 5  # 分页5条一分页

    # 添加、修改页属性
    fields = ['name',  'img', 'trackid','isDelete']  # 添加数据显示的顺序
    # fieldsets = []    不能与fields同时使用，二选一，是一个分组,元组

#注册小轮播图
@admin.register(Mustbuy)  #注册
class MustbuyAdmin(admin.ModelAdmin):  # 类需要在需要的表里注册一下
    # 列表属性
    list_display = ['pk', 'img',  'name', 'trackid', 'isDelete']  # 显示列表的列
    list_filter = ['name','isDelete']  # 右侧增加过滤条件
    search_fields = ['name']  # 添加搜索框，按sname搜索,多加多条件
    list_per_page = 5  # 分页5条一分页

    # 添加、修改页属性
    fields = ['name',  'img', 'trackid','isDelete']  # 添加数据显示的顺序
    # fieldsets = []    不能与fields同时使用，二选一，是一个分组,元组

#注册商品分类
@admin.register(Foodtypes)  #注册
class FoodtypesAdmin(admin.ModelAdmin):  # 类需要在需要的表里注册一下
    # 列表属性
    list_display = ['pk', 'typeid',  'typename', 'childtypenames', 'typesort','idDelete']  # 显示列表的列
    list_filter = ['typename','idDelete']  # 右侧增加过滤条件
    search_fields = ['typename']  # 添加搜索框，按sname搜索,多加多条件
    list_per_page = 5  # 分页5条一分页

    # 添加、修改页属性
    fields = ['typeid',  'typename', 'childtypenames', 'typesort','idDelete']  # 添加数据显示的顺序
    # fieldsets = []    不能与fields同时使用，二选一，是一个分组,元组

#注册商品
@admin.register(Goods)  #注册
class GoodsAdmin(admin.ModelAdmin):  # 类需要在需要的表里注册一下
    # 列表属性
    list_display = ['pk', 'productid',  'productimg', 'productname', 'productlongname', 'isxf','pmdesc','specifics','price','marketprice','categoryid','childcid','childcidname','dealerid','storenums','productnum']  # 显示列表的列
    list_filter = ['productname']  # 右侧增加过滤条件
    search_fields = ['productname']  # 添加搜索框，按sname搜索,多加多条件
    list_per_page = 5  # 分页5条一分页

    # 添加、修改页属性
    fields = ['productid',  'productimg', 'productname', 'productlongname', 'isxf','pmdesc','specifics','price','marketprice','categoryid','childcid','childcidname','dealerid','storenums','productnum']  # 添加数据显示的顺序
    # fieldsets = []    不能与fields同时使用，二选一，是一个分组,元组

#注册用户
@admin.register(User)  #注册
class UserAdmin(admin.ModelAdmin):  # 类需要在需要的表里注册一下
    # 列表属性
    list_display = ['pk', 'userAccount', 'userName', 'userPasswd', 'userPhone','userAddress','userImg','userRank']  # 显示列表的列
    list_filter = ['userAccount', 'userName']  # 右侧增加过滤条件
    search_fields = ['userAccount', 'userName']  # 添加搜索框，按sname搜索,多加多条件
    list_per_page = 5  # 分页5条一分页

    # 添加、修改页属性
    fields = ['userAccount', 'userName', 'userPasswd', 'userPhone','userAddress','userImg','userRank']  # 添加数据显示的顺序
    # fieldsets = []    不能与fields同时使用，二选一，是一个分组,元组


