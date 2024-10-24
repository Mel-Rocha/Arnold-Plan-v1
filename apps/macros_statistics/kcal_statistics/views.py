from django.shortcuts import render, get_object_or_404

from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros_statistics.kcal_statistics.utils import get_kcal_tuples


def view_kcal_tuples(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    kcal_tuples = get_kcal_tuples(macros_planner)

    print(kcal_tuples)  # Adicione esta linha para debug
    context = {'macros_planner': macros_planner, 'kcal_tuples': kcal_tuples}
    return render(request, 'kcal_statistics/kcal_tuples.html', context)
