from django.urls import path
from .views import CustomLoginView, dashboard

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]