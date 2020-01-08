from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView    #解决favicon.ico

urlpatterns = [
    url(r'^$', views.home),
    url(r'^index$', views.index),
    url(r'^index.html',views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    url(r'^mime/$', views.mime, name='mime'),
    url(r'^base/$',views.base,name='base'),
    # url(r'^default',views.default),   #测试轮播使用
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    # url(r'^saveuser/$',views.saveuser,name='saveuser'),

    #验证账号是否被注册
    url(r'^checkuserid/$',views.checkuserid,name='checkuserid'),
    url(r'^quit/$',views.quit,name='quit'),
    url(r'^changecart/(\d+)/$',views.changecart,name='changecart'),



    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),

]

