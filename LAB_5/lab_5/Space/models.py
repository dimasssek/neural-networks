from django.db import models


class Planet(models.Model):
    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"

    planetId = models.AutoField(verbose_name='ID планеты', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Название планеты', max_length=255)
    number_of_satellites = models.IntegerField(verbose_name='Количество спутников')

    def __str__(self):
        return str(self.name)

class Astronaut(models.Model):
    class Meta:
        verbose_name = "Астронавт"
        verbose_name_plural = "Астронавты"

    astronautId = models.AutoField(verbose_name='ID астронавта', primary_key=True, unique=True)
    fio = models.CharField(verbose_name='ФИО астронавта', max_length=255)
    age = models.IntegerField(verbose_name='Возраст астронавта')
    number_of_flights = models.IntegerField(verbose_name='Количество полётов астронавта')

    def __str__(self):
        return str(self.fio)

class Expedition(models.Model):
    class Meta:
        verbose_name = "Экспедиция"
        verbose_name_plural = "Экспедиции"

    expeditionId = models.AutoField(verbose_name='ID экспедиции', primary_key=True, unique=True)
    report = models.CharField(verbose_name='Описание экспедиции', max_length=255)
    expedition_time = models.CharField(verbose_name='Время экспедиции', max_length=255)
    planetId = models.ForeignKey(Planet, verbose_name='ID планеты', on_delete=models.SET(-1))
    astronautId = models.ForeignKey(Astronaut, verbose_name='ID астронавта', on_delete=models.SET(-1))

    def get_absolute_url(self):
        return f'/{self.expeditionId}/change'

    def __str__(self):
        return f"Экспедиция - {self.expedition_time} {self.report}"
