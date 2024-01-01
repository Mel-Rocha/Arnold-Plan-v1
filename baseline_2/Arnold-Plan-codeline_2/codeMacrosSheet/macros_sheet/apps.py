from django.apps import AppConfig


class MacrosSheetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'macros_sheet'


    def ready(self):
        import macros_sheet.signals 