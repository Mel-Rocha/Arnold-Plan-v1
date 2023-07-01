from django.shortcuts import render, redirect, get_object_or_404
from .models import MacrosPlanner
from .forms import MacrosPlannerForm
from general_info.forms import GeneralInfoForm 
#from .forms import GeneralInfoInlineForm
from django.contrib.auth.decorators import login_required

@login_required
def macros_planner_list(request):
    profile = request.user.profile
    print("Perfil:", profile)
    macros_planners = MacrosPlanner.objects.filter(profile__user=request.user)
    print("Macros Planners:", macros_planners)
    return render(request, 'macros_planner/macros_planner_list.html', {'macros_planners': macros_planners})

@login_required
def macros_planner_create(request):
    if request.method == 'POST':
        general_info_form = GeneralInfoForm(request.POST)
        if general_info_form.is_valid():
            general_info = general_info_form.save(commit=False)
            macros_planner = MacrosPlanner(profile=request.user.profile)
            macros_planner.save()
            general_info.macros_planner = macros_planner
            general_info.save()
            return redirect('macros_planner:macros_planner_details', pk=macros_planner.pk)
    else:
        general_info_form = GeneralInfoForm()
    return render(request, 'macros_planner:macros_planner_create.html', {'general_info_form': general_info_form})


@login_required
def macros_planner_update(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    if request.method == 'POST':
        form = MacrosPlannerForm(request.POST, instance=macros_planner)
        if form.is_valid():
            form.save()
            return redirect('macros_planner_details', pk=macros_planner.pk)
    else:
        form = MacrosPlannerForm(instance=macros_planner)
    return render(request, 'macros_planner/macros_planner_update.html', {'form': form, 'macros_planner': macros_planner})

@login_required
def macros_planner_delete(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    if request.method == 'POST':
        macros_planner.delete()
        return redirect('macros_planner_list')
    return render(request, 'macros_planner/macros_planner_delete.html', {'macros_planner': macros_planner})

@login_required
def macros_planner_details(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    return render(request, 'macros_planner/macros_planner_details.html', {'macros_planner': macros_planner})
