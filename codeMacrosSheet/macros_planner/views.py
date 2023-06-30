from django.shortcuts import render, redirect, get_object_or_404
from .models import MacrosPlanner
from .forms import MacrosPlannerForm

def macros_planner_list(request):
    macros_planners = MacrosPlanner.objects.all()
    return render(request, 'macros_planner/macros_planner_list.html', {'macros_planners': macros_planners})


def macros_planner_create(request):
    if request.method == 'POST':
        form = MacrosPlannerForm(request.POST)
        if form.is_valid():
            macros_planner = form.save()
            return redirect('macros_planner_details', pk=macros_planner.pk)
    else:
        form = MacrosPlannerForm()
    return render(request, 'macros_planner_create.html', {'form': form})

def macros_planner_update(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    if request.method == 'POST':
        form = MacrosPlannerForm(request.POST, instance=macros_planner)
        if form.is_valid():
            form.save()
            return redirect('macros_planner_details', pk=macros_planner.pk)
    else:
        form = MacrosPlannerForm(instance=macros_planner)
    return render(request, 'macros_planner_update.html', {'form': form, 'macros_planner': macros_planner})

def macros_planner_delete(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    if request.method == 'POST':
        macros_planner.delete()
        return redirect('macros_planner_list')
    return render(request, 'macros_planner_delete.html', {'macros_planner': macros_planner})

def macros_planner_details(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    return render(request, 'macros_planner_details.html', {'macros_planner': macros_planner})
