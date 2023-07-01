from django.shortcuts import render, get_object_or_404, redirect
from .models import MacrosSheet
from .forms import MacrosSheetForm

def macros_sheet_update(request, pk):
    macros_sheet = get_object_or_404(MacrosSheet, pk=pk)
    if request.method == 'POST':
        form = MacrosSheetForm(request.POST, instance=macros_sheet)
        if form.is_valid():
            form.save()
            return redirect('macros_planner:macros_sheet_details', pk=macros_sheet.pk)
    else:
        form = MacrosSheetForm(instance=macros_sheet)
    return render(request, 'macros_planner/macros_sheet_update.html', {'form': form, 'macros_sheet': macros_sheet})

def macros_sheet_details(request, pk):
    macros_sheet = get_object_or_404(MacrosSheet, pk=pk)
    return render(request, 'macros_planner/macros_sheet_details.html', {'macros_sheet': macros_sheet})


def macros_sheet_list(request):
    macros_sheets = MacrosSheet.objects.all()
    return render(request, 'macros_planner/macros_sheet_list.html', {'macros_sheets': macros_sheets})