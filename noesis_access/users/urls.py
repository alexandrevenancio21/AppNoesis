from django.urls import path
from .views import CustomLoginView, homepage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('homepage/', homepage, name='homepage'),
]