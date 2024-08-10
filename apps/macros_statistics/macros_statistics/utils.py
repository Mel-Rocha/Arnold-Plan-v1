def get_macros_tuples(macros_planner):
    # Obtém todas as MacrosSheets associadas a um MacrosPlanner específico, ordenadas por id (ordem de criação)
    macros_sheets = macros_planner.macrossheet_set.all().order_by('id')

    # Cria as tuplas desejadas com ID da MacrosSheet, cho, calcs, e fat
    macros_tuples = [
        (macros_sheet.week, macros_sheet.cho, macros_sheet.ptn, macros_sheet.fat) for macros_sheet in macros_sheets
    ]

    return macros_tuples


def get_macros_pie_data(macros_sheet):
    data = {
        'labels': ['CHO', 'PTN', 'FAT'],
        'datasets': [
            {
                'data': [macros_sheet.cho, macros_sheet.ptn, macros_sheet.fat],
                'backgroundColor': ['rgba(255, 0, 0, 0.5)', 'rgba(0, 255, 0, 0.5)', 'rgba(0, 0, 255, 0.5)'],
            },
        ],
    }

    return data
