def get_kcal_tuples(macros_planner):
    # Obtém todas as MacrosSheets associadas a um MacrosPlanner específico, ordenadas por id (ordem de criação)
    macros_sheets = macros_planner.macrossheet_set.all().order_by('id')

    # Atualiza o campo week com base no ID se ainda não estiver atualizado
    for index, macros_sheet in enumerate(macros_sheets):
        if macros_sheet.week == 0:
            macros_sheet.week = index + 1
            macros_sheet.save()

    # Cria as tuplas desejadas com número de semana e kcal
    kcal_tuples = [
        (macros_sheet.week, macros_sheet.kcal) for macros_sheet in macros_sheets
    ]

    return kcal_tuples