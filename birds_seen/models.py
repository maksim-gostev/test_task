from django.db import models

from birds.models import Birds


class Birds_seen(models.Model):
    birds = models.ForeignKey(Birds, on_delete=models.CASCADE, related_name='birds_seen',
                              verbose_name='Увиденные птицы')
    updated = models.DateTimeField(verbose_name='Дата последнего обновления')
    number_vision_acts = models.IntegerField(verbose_name='Количество актов видения', default=1)
