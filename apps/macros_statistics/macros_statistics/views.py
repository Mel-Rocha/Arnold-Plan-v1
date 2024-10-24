from django.shortcuts import render, get_object_or_404

from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros_statistics.macros_statistics.utils import get_macros_tuples


def view_macros_tuples(request, pk):
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    macros_tuples = get_macros_tuples(macros_planner)

    print(macros_tuples)  # Adicione esta linha para debug
    context = {'macros_planner': macros_planner, 'macros_tuples': macros_tuples}
    return render(request, 'macros_statistics/macros_tuples.html', context)
