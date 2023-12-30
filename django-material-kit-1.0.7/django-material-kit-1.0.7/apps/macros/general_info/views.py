from django.shortcuts import render, redirect, get_object_or_404
from .models import GeneralInfo
from .forms import GeneralInfoForm
from django.contrib.auth.decorators import login_required
from apps.macros.macros_sheet.models import MacrosSheet

@login_required
def general_info_create(request):
    if request.method == 'POST':
        form = GeneralInfoForm(request.POST)
        if form.is_valid():
            general_info = form.save()
            return redirect('general_info:general_info_details', pk=general_info.pk)
    else:
        form = GeneralInfoForm()
    return render(request, 'general_info/general_info_create.html', {'form': form})

@login_required
def general_info_update(request, pk):
    general_info = get_object_or_404(GeneralInfo, pk=pk)

    if request.method == 'POST':
        form = GeneralInfoForm(request.POST, instance=general_info)
        if form.is_valid():
            general_info = form.save()
            return redirect('general_info:general_info_details', pk=general_info.pk)
    else:
        form = GeneralInfoForm(instance=general_info)
    
    return render(request, 'general_info/general_info_update.html', {'form': form, 'general_info': general_info})


@login_required
def general_info_delete(request, pk):
    general_info = get_object_or_404(GeneralInfo, pk=pk)
    if request.method == 'POST':
        general_info.delete()
        return redirect('general_info:general_info_list')
    return render(request, 'general_info/general_info_delete.html', {'general_info': general_info})

@login_required
def general_info_details(request, pk):
    general_info = get_object_or_404(GeneralInfo, pk=pk)
    return render(request, 'general_info/general_info_details.html', {'general_info': general_info})

