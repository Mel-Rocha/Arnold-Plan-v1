from macros_planner.models import MacrosPlanner  # Importe o modelo MacrosPlanner
from macros_sheet.models import MacrosSheet  # Importe o modelo MacrosSheet

def get_kcal_tuples(macros_planner):
    # Obtém todas as MacrosSheets associadas a um MacrosPlanner específico, ordenadas por id (ordem de criação)
    macros_sheets = macros_planner.macrossheet_set.all().order_by('id')

    # Cria as tuplas desejadas com número de semana fictício (aqui, usando a ordem de criação) e kcal
    kcal_tuples = [
        (index + 1, macros_sheet.kcal) for index, macros_sheet in enumerate(macros_sheets)
    ]

    return kcal_tuples