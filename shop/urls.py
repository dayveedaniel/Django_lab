from django.template.defaulttags import url
from django.urls import path, re_path
from .views import HomePageView, CustomersListView, OrdersListView, SearchView, product_list, product_detail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('search', SearchView.as_view(), name='search'),
    # path('', product_list, name='product_list'),
    # re_path(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
    # path('posts/<slug:slug>/', posts_detail, name='unique_slug'),
    # url(r'^$', product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     product_list,
    #     name='product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    #     product_detail,
    #     name='product_detail'),
]
