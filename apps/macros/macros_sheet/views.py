from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from apps.macros.macros_sheet.models import MacrosSheet
from apps.macros.macros_sheet.forms import MacrosSheetForm
from apps.macros.macros_planner.models import MacrosPlanner


@login_required
def macros_sheet_create(request, macros_planner_id):
    macros_planner = MacrosPlanner.objects.get(pk=macros_planner_id)

    if request.method == 'POST':
        form = MacrosSheetForm(request.POST)
        if form.is_valid():
            macros_sheet = form.save(commit=False)
            macros_sheet.macros_planner = macros_planner
            macros_sheet.save()
            return redirect('macros_sheet:macros_sheet_details', pk=macros_sheet.pk)
    else:
        form = MacrosSheetForm()
    return render(request, 'macros_sheet/macros_sheet_create.html', {'form': form})


@login_required
def macros_sheet_update(request, pk):
    macros_sheet = get_object_or_404(MacrosSheet, pk=pk)
    if request.method == 'POST':
        form = MacrosSheetForm(request.POST, instance=macros_sheet)
        if form.is_valid():
            form.save()
            return redirect('macros_sheet:macros_sheet_details', pk=macros_sheet.pk)
    else:
        form = MacrosSheetForm(instance=macros_sheet)
    return render(request, 'macros_sheet/macros_sheet_update.html', {'form': form, 'macros_sheet': macros_sheet})


@login_required
def macros_sheet_details(request, pk):
    macros_sheet = get_object_or_404(MacrosSheet, pk=pk)
    return render(request, 'macros_sheet/macros_sheet_details.html', {'macros_sheet': macros_sheet})


@login_required
def macros_sheet_list(request):
    macros_sheets = MacrosSheet.objects.all()
    return render(request, 'macros_sheet/macros_sheet_list.html', {'macros_sheets': macros_sheets})


@login_required
def macros_sheet_delete(request, pk):
    macros_sheet = get_object_or_404(MacrosSheet, pk=pk)
    macros_planner = macros_sheet.macros_planner  # Obter o MacrosPlanner relacionado

    if request.method == 'POST':
        macros_sheet.delete()
        return redirect('macros_planner:macros_planner_details', pk=macros_planner.pk)

    return render(request, 'macros_sheet/macros_sheet_delete.html', {'macros_sheet': macros_sheet})
