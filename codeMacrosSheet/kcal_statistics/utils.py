def get_kcal_tuples(macros_planner):
    # Obtém todas as MacrosSheets associadas a um MacrosPlanner específico, ordenadas por id (ordem de criação)
    macros_sheets = macros_planner.macrossheet_set.all().order_by('id')

    # Cria as tuplas desejadas com número de semana e kcal
    kcal_tuples = [
        (macros_sheet.week, macros_sheet.kcal) for macros_sheet in macros_sheets
    ]

    return kcal_tuples

