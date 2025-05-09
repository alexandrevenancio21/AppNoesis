from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import handler404

from .views import (
    CustomLoginView,
    homepage,
    clientList,
    pii,
    testingOn,
    vqm,
    suppliers,
    lowCode,
    manuals,
    unauthorized,
)

# Define your URL patterns
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('homepage/', homepage, name='homepage'),

    # Ativos com controlo de permissões
    path('ativos/clientList/', clientList, name='client_list'),
    path('ativos/pii/', pii, name='pii'),
    path('ativos/testingOn/', testingOn, name='testing_on'),
    path('ativos/vqm/', vqm, name='vqm'),
    path('ativos/suppliers/', suppliers, name='suppliers'),
    path('ativos/lowCode/', lowCode, name='low_code'),
    path('ativos/manuals/', manuals, name='manuals'),

    # Página de erro
    path('unauthorized/', unauthorized, name='unauthorized'),

    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),
]
