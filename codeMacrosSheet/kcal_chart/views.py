from django.shortcuts import render, get_object_or_404
from macros_planner.models import MacrosPlanner
from .utils import get_kcal_tuples  # Ajuste a importação se necessário
#from .utils import generate_kcal_chart


def kcal_chart_view(request, pk):
    # Obtenha os dados necessários para o gráfico usando o pk do MacrosPlanner
    macros_planner = get_object_or_404(MacrosPlanner, pk=pk)
    kcal_tuples = get_kcal_tuples(macros_planner)

    # Passe os dados para o template
    context = {'macros_planner': macros_planner, 'kcal_tuples': kcal_tuples}
    
    return render(request, 'kcal_chart/kcal_chart.html', context)