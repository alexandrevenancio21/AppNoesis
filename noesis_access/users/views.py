from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Login View com template específico
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Deve corresponder a users/templates/login.html

# Página do dashboard
@login_required
def dashboard(request):
    user = request.user
    grupo = user.groups.first().name if user.groups.exists() else "sem_grupo"
    return render(request, 'dashboard.html', {'user': user, 'grupo': grupo})