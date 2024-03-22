from django.urls import path
from .views import HomePageView, CustomersListView, ticker_details

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('ticker/<slug:slug>/', ticker_details, name='details'),
]
