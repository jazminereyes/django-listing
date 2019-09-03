from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.blog_view, name='blog_view'),
    url(r'^my/blog/(?P<user_id>[0-9]+)/$', views.blog_user, name='blog_user'),
    url(r'^blog/new/$', views.blog_new, name='blog_new'),
    url(r'^blog/update/(?P<blog_id>[0-9]+)/$', views.blog_edit, name='blog_edit'),
    url(r'^blog/delete/(?P<blog_id>[0-9]+)/$', views.blog_remove, name='blog_remove'),
    url(r'^products/$', views.shop, name='shop'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.shop_view, name='shop_view'),
    url(r'^my/products/(?P<user_id>[0-9]+)/$', views.shop_user, name='shop_user'),
    url(r'^products/new/$', views.shop_new, name='shop_new'),
    url(r'^products/update/(?P<product_id>[0-9]+)/$', views.shop_edit, name='shop_edit'),
    url(r'^products/delete/(?P<product_id>[0-9]+)/$', views.shop_remove, name='shop_remove'),
    url(r'^inquiries/$', views.inquiry, name='inquiry'),
    url(r'^inquiries/(?P<inquiry_id>[0-9]+)/$', views.inquiry_view, name='inquiry_view'),
    url(r'^my/inquiries/(?P<user_id>[0-9]+)/$', views.inquiry_user, name='inquiry_user'),
    url(r'^inquiries/new/$', views.inquiry_new, name='inquiry_new'),
    url(r'^inquiries/update/(?P<inquiry_id>[0-9]+)/$', views.inquiry_edit, name='inquiry_edit'),
    url(r'^inquiries/delete/(?P<inquiry_id>[0-9]+)/$', views.inquiry_remove, name='inquiry_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)