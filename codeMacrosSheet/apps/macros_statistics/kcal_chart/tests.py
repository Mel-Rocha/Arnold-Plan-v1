#<<CERTO mass como vamos pegar o macrosPlanner dinamicamente>>
import matplotlib.pyplot as plt
from kcal_statistics.utils import get_kcal_tuples
from macros_planner.models import MacrosPlanner

# Substitua 'seu_pk_aqui' pelo ID real do MacrosPlanner desejado
macros_planner_pk = 25

# Obtenha a instância do MacrosPlanner
macros_planner = MacrosPlanner.objects.get(pk=macros_planner_pk)

# Chame a função para obter as tuplas dinâmicas
dynamic_kcal_tuples = get_kcal_tuples(macros_planner)

# Verifique se as tuplas estão corretas
print(dynamic_kcal_tuples)

# Extraia os valores de x e y das tuplas
x_values, y_values = zip(*dynamic_kcal_tuples)

# Crie o gráfico usando matplotlib
plt.plot(x_values, y_values, marker='o')
plt.xlabel('Semana')
plt.ylabel('Kcal')
plt.title('Evolução das Kcal ao longo das Semanas (Matplotlib)')
plt.show()