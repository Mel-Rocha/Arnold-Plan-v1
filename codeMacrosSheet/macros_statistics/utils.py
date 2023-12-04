from macros_planner.models import MacrosPlanner  # Importe o modelo MacrosPlanner
from macros_sheet.models import MacrosSheet

def get_macros_tuples(macros_planner):
    # Obtém todas as MacrosSheets associadas a um MacrosPlanner específico, ordenadas por id (ordem de criação)
    macros_sheets = macros_planner.macrossheet_set.all().order_by('id')

    # Cria as tuplas desejadas com ID da MacrosSheet, cho, ptn, e fat
    macros_tuples = [
        (macros_sheet.week, macros_sheet.cho, macros_sheet.ptn, macros_sheet.fat) for macros_sheet in macros_sheets
    ]

    return macros_tuples