from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import user_passes_test

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/users/homepage' 

@login_required
def homepage(request):
    user = request.user
    grupo = user.groups.first().name if user.groups.exists() else "sem_grupo"
    return render(request, 'homepage.html', {'user': user, 'grupo': grupo})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            user.groups.add(group)
            login(request, user)  
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def group_required(*group_names):
    def check(user):
        return user.is_authenticated and (user.is_superuser or user.groups.filter(name__in=group_names).exists())
    return user_passes_test(check, login_url='/users/unauthorized/')

def unauthorized(request):
    return render(request, 'error.html', status=403)

def custom_page_not_found(request, exception):
    return render(request, 'error404.html', status=404)

    

#Views para Segurança
@group_required('comerciais', 'financeiro', 'admin')
def clientList(request):
    return render(request, 'ativos/clientList.html')

@group_required('developers', 'admin')
def lowCode(request):
    return render(request, 'ativos/lowCode.html')

@group_required('developers', 'admin')
def manuals(request):
    return render(request, 'ativos/manuals.html')

@group_required('RH', 'admin')
def pii(request):
    return render(request, 'ativos/pii.html')

@group_required('financeiro', 'admin')
def suppliers(request):
    return render(request, 'ativos/suppliers.html')

@group_required('developers', 'admin')
def testingOn(request):
    return render(request, 'ativos/testingOn.html')

@group_required('developers', 'admin')
def vqm(request):
    return render(request, 'ativos/vqm.html')

