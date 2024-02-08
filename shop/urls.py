from django.urls import path, re_path
from .views import HomePageView, CustomersListView, OrdersListView, ticker_details

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('ticker/<slug:slug>/', ticker_details, name='details'),
]
