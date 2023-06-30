from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

from allauth.account.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.profile:
            return reverse_lazy('profile_:profile_details')
        else:
            return reverse_lazy('profile_:profile_create')

@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associar o usuário atualmente logado ao perfil
            profile.save()
            return redirect('profile_:profile_details')
    else:
        form = ProfileForm()
    return render(request, 'profile_/profile_create.html', {'form': form})

@login_required
def profile_update(request, pk):
    profile = get_object_or_404(Profile, user=request.user, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_:profile_details', pk=pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_/profile_update.html', {'form': form, 'profile': profile})

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, user=request.user, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_:profile_create')
    return render(request, 'profile_/profile_delete.html', {'profile': profile})

@login_required
def profile_details(request, pk):
    profile = get_object_or_404(Profile, user=request.user, pk=pk)
    return render(request, 'profile_/profile_details.html', {'profile': profile})