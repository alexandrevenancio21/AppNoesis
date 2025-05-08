from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.views.generic.base import TemplateView

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/users/homepage/'  # Redireciona para a homepage após login

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
            login(request, user)  # opcional: login automático
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})