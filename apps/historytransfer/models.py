from django.db import models


# Create your models here.
from apps.users.models import User

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="from_user",
        verbose_name="От пользователя"
    )
    to_user = models.ForeignKey(
        User
        ,
        on_delete=models.CASCADE,
        related_name="to_user",
        verbose_name="Пользователю"
    )
    is_complated = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    amount = models.CharField(
        max_length=255,
        verbose_name="Сумма"
    )
    def __str__ (self):
        return self.amount
    
    class Meta:
        verbose_name = "История перевода"
        verbose_name_plural = "История переводов"