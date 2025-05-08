from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .views import CustomLoginView, homepage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('homepage/', homepage, name='homepage'),
    path('ativos/clientList/', TemplateView.as_view(template_name='ativos/clientList.html'), name='client_list'),
    path('ativos/pii/', TemplateView.as_view(template_name='ativos/pii.html'), name='pii'),
    path('ativos/testingOn/', TemplateView.as_view(template_name='ativos/testingOn.html'), name='testing_on'),
    path('ativos/customers/', TemplateView.as_view(template_name='ativos/customers.html'), name='customers'),
    path('ativos/vqm/', TemplateView.as_view(template_name='ativos/vqm.html'), name='vqm'),
    path('ativos/suppliers/', TemplateView.as_view(template_name='ativos/suppliers.html'), name='suppliers'),
    path('ativos/lowCode/', TemplateView.as_view(template_name='ativos/lowCode.html'), name='low_code'),
    path('ativos/manuals/', TemplateView.as_view(template_name='ativos/manuals.html'), name='manuals'),
    path('logout/', LogoutView.as_view(), name='logout'),
    

]