from django.shortcuts import render

from apps.macros.macros_sheet.models import MacrosSheet
from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros_statistics.macros_statistics.utils import get_macros_tuples
from apps.macros_statistics.macros_statistics.utils import get_macros_pie_data


def macros_pie_chart_view(request, sheet_id):
    macros_sheet = MacrosSheet.objects.get(pk=sheet_id)
    pie_data = get_macros_pie_data(macros_sheet)

    return render(request, 'macros_chart/macros_pie_chart.html', {'data': pie_data})


def macros_chart_view(request, pk):
    macros_planner = MacrosPlanner.objects.get(pk=pk)
    macros_tuples = get_macros_tuples(macros_planner)

    data = {
        'labels': [f'Semana {week}' for week, _, _, _ in macros_tuples],
        'datasets': [
            {
                'label': 'CHO',
                'backgroundColor': 'rgba(183, 14, 11, 1.0)',
                'data': [cho for _, cho, _, _ in macros_tuples],
            },
            {
                'label': 'PTN',
                'backgroundColor': 'rgba(238, 181, 94, 1.0)',
                'data': [ptn for _, _, ptn, _ in macros_tuples],
            },
            {
                'label': 'FAT',
                'backgroundColor': 'rgba(100, 100, 100, 0.5)',
                'data': [fat for _, _, _, fat in macros_tuples],
            },
        ],
    }

    return render(request, 'macros_chart/macros_chart.html', {'data': data})
