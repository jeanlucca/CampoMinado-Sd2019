from django.db import models
from django.utils import timezone

class Jogada(models.Model):
    linha = models.CharField(max_length=3)
    coluna = models.CharField(max_length=3)
    created_date = models.DateTimeField(default=timezone.now)
