from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name= "Ваша почта",
        unique=True
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name= "дата перевода"
    )
    age = models.IntegerField(
        verbose_name="Возраст",
        blank=True,
        null=True
    )
    balance = models.CharField(
        max_length=255,
        verbose_name="Баланс",
        blank=True,
        null=True
    )
    vallet_adress = models.CharField(
        max_length=12,
        verbose_name="Кошелек",
        blank=True,
        null=True,
        unique=True
    )
    # def __str__(self):
    #     return self.vallet_adress 
    
    class Meta:
        verbose_name = "Ползователь"
        verbose_name_plural = "Ползователи"

    def save(self, *args, **kwargs):
        if not self.vallet_adress:
            self.vallet_adress = secrets.token_hex(6)
        super().save(*args, **kwargs)