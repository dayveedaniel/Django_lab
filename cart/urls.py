from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.SignUp.as_view(), name='signup'),
]
