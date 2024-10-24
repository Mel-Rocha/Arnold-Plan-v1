from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros_statistics.kcal_statistics.utils import get_kcal_tuples


def kcal_chart_view(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    kcal_tuples = get_kcal_tuples(macros_planner)

    data = {
        'labels': [f'Semana {week}' for week, _ in kcal_tuples],
        'data': [kcal for _, kcal in kcal_tuples],
    }

    return render(request, 'kcal_chart/kcal_chart.html', {
        'data': data,
    })
