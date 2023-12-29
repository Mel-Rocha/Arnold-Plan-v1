#Digita isso no terminal python manage.py shell
# Importe o modelo MacrosPlanner e a função get_kcal_tuples
from macros_planner.models import MacrosPlanner
from kcal_statistics.utils import get_kcal_tuples

# Substitua '25' pelo ID real do MacrosPlanner que você deseja verificar
macros_planner_id = 25

# Obtenha o MacrosPlanner específico
macros_planner = MacrosPlanner.objects.get(id=macros_planner_id)

# Use a função get_kcal_tuples para obter as tuplas de Kcal
kcal_tuples = get_kcal_tuples(macros_planner)

# Exiba as tuplas
print(kcal_tuples)
