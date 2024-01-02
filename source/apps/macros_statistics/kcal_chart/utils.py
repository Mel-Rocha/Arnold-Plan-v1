import matplotlib.pyplot as plt
from macros_planner.models import MacrosPlanner
from kcal_statistics.utils import get_kcal_tuples
import io

from django.shortcuts import get_object_or_404
from .models import MacrosPlanner
from .utils import get_kcal_tuples

def generate_kcal_chart(macros_planner_pk):
    # Obtenha a instância do MacrosPlanner usando o pk
    macros_planner = get_object_or_404(MacrosPlanner, pk=macros_planner_pk)

    # Chame a função para obter as tuplas dinâmicas
    dynamic_kcal_tuples = get_kcal_tuples(macros_planner)

    # Extraia os valores de x e y das tuplas
    x_values, y_values = zip(*dynamic_kcal_tuples)

    # Crie o gráfico usando matplotlib
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Semana')
    plt.ylabel('Kcal')
    plt.title('Evolução das Kcal ao longo das Semanas (Matplotlib)')
    plt.show()
