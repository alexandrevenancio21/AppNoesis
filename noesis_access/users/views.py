from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
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