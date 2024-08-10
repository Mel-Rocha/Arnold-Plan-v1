from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.macros.macros_sheet.models import MacrosSheet
from apps.macros.general_info.forms import GeneralInfoForm
from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros.macros_planner.forms import MacrosPlannerForm
from apps.macros_statistics.kcal_statistics.utils import get_kcal_tuples


@login_required
def macros_planner_list(request):
    profile = request.user.profile
    print("Perfil:", profile)
    macros_planners = MacrosPlanner.objects.filter(profile__user=request.user)
    print("Macros Planners:", macros_planners)
    return render(request, 'macros_planner/macros_planner_list.html',
                  {'profile': profile, 'macros_planners': macros_planners})


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

            macros_sheet = MacrosSheet(macros_planner=macros_planner)
            macros_sheet.save()

            return redirect('macros_planner:macros_planner_details', pk=macros_planner.pk)  #NÃO TIRA OS :
    else:
        general_info_form = GeneralInfoForm()
    return render(request, 'macros_planner/macros_planner_create.html', {'general_info_form': general_info_form})


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
    return render(request, 'macros_planner/macros_planner_update.html',
                  {'form': form, 'macros_planner': macros_planner})


@login_required
def macros_planner_delete(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    if request.method == 'POST':
        macros_planner.delete()
        return redirect('macros_planner:macros_planner_list')
    return render(request, 'macros_planner/macros_planner_delete.html', {'macros_planner': macros_planner})


@login_required
def macros_planner_details(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    general_info = macros_planner.generalinfo  # Usar o relacionamento inverso
    macros_sheets = macros_planner.macrossheet_set.all()

    kcal_tuples = get_kcal_tuples(macros_planner)

    context = {'macros_planner': macros_planner, 'general_info': general_info, 'macros_sheets': macros_sheets,
               'kcal_tuples': kcal_tuples}
    return render(request, 'macros_planner/macros_planner_details.html', context)
