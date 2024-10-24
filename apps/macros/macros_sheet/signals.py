import logging
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from apps.macros.macros_sheet.models import MacrosSheet

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=MacrosSheet)
def pre_delete_macros_sheet(sender, instance, **kwargs):
    logger.info(f"Signal received for MacrosSheet {instance.id} deletion.")
    instance.update_week_based_on_id()
