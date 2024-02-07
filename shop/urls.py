from django.template.defaulttags import url
from django.urls import path, re_path
from .views import HomePageView, CustomersListView, OrdersListView, ProductsListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('ticker/<slug:slug>/', ProductsListView.as_view(), name='details'),  # Add this line
]
