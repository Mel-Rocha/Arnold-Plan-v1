from django.shortcuts import render, redirect, get_object_or_404
from .models import GeneralInfo
from .forms import GeneralInfoForm
from django.contrib.auth.decorators import login_required
from macros_sheet.models import MacrosSheet

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
            general_info = form.save(commit=False)
            general_info.save()

            # Atualizar o número de MacrosSheets
            macros_planner = general_info.macros_planner
            weeks = general_info.weeks
            current_weeks = macros_planner.macros_sheets.count()

            if weeks > current_weeks:
                # Criar MacrosSheets adicionais
                for week in range(current_weeks + 1, weeks + 1):
                    macros_sheet = MacrosSheet(
                        macros_planner=macros_planner,
                        week_number=week,
                        # Defina os valores de CHO, PTN, FAT e Kcal de acordo com sua lógica
                    )
                    macros_sheet.save()
            elif weeks < current_weeks:
                # Excluir MacrosSheets adicionais
                MacrosSheet.objects.filter(macros_planner=macros_planner, week_number__gt=weeks).delete()

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

