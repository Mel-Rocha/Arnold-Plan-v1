from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.user.profile_.models import Profile


def homepage(request):
    return render(request=request,
                  template_name= 'home.html',)


@login_required
def dashboard(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        # O usuário possui um perfil, redirecionar para a página desejada
        return render(request, 'dashboard/dashboard.html', {'profile': profile})

    except Profile.DoesNotExist:
        # O usuário não possui um perfil, redirecionar para a página de criação de perfil
        return redirect('profile_:profile_create')