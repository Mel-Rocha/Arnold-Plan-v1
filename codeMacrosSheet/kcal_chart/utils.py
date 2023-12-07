import matplotlib.pyplot as plt
from macros_planner.models import MacrosPlanner
from kcal_statistics.utils import get_kcal_tuples
import io



def generate_kcal_chart(macros_planner):

    # Obtenha a instância do MacrosPlanner
    macros_planner = MacrosPlanner.objects.get(pk=macros_planner)
    print("ta funcionando")

    # Chame a função para obter as tuplas dinâmicas
    dynamic_kcal_tuples = get_kcal_tuples(macros_planner.id)
    #print(dynamic_kcal_tuples)

    # Extraia os valores de x e y das tuplas
    x_values, y_values = zip(*dynamic_kcal_tuples)

    # Crie o gráfico usando matplotlib
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Semana')
    plt.ylabel('Kcal')
    plt.title('Evolução das Kcal ao longo das Semanas (Matplotlib)')

    # Salve o gráfico como uma imagem em BytesIO
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    # Retorne o stream de BytesIO
    return image_stream

    