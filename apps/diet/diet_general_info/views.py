from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import DietGeneralInfo
from apps.diet.diet_general_info.forms import DietGeneralInfoForm


@login_required
def diet_general_info_create(request):
    if request.method == 'POST':
        form = DietGeneralInfoForm(request.POST)
        if form.is_valid():
            diet_general_info = form.save()
            return redirect('diet_general_info:diet_general_info_details', pk=diet_general_info.pk)
    else:
        form = DietGeneralInfoForm()
    return render(request, 'diet_general_info/diet_general_info_create.html', {'form': form})


@login_required
def diet_general_info_update(request, pk):
    diet_general_info = get_object_or_404(DietGeneralInfo, pk=pk)

    if request.method == 'POST':
        form = DietGeneralInfoForm(request.POST, instance=diet_general_info)
        if form.is_valid():
            diet_general_info = form.save()
            return redirect('diet_general_info:diet_general_info_details', pk=diet_general_info.pk)
    else:
        form = DietGeneralInfoForm(instance=diet_general_info)
    
    return render(request, 'diet_general_info/diet_general_info_update.html', {'form': form, 'diet_general_info': diet_general_info})


@login_required
def diet_general_info_delete(request, pk):
    diet_general_info = get_object_or_404(DietGeneralInfo, pk=pk)
    if request.method == 'POST':
        diet_general_info.delete()
        return redirect('diet_general_info:diet_general_info_list')
    return render(request, 'diet_general_info/diet_general_info_delete.html', {'diet_general_info': diet_general_info})


@login_required
def diet_general_info_details(request, pk):
    diet_general_info = get_object_or_404(DietGeneralInfo, pk=pk)
    return render(request, 'diet_general_info/diet_general_info_details.html', {'diet_general_info': diet_general_info})
