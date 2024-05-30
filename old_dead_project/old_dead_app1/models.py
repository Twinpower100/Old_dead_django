from django.db import models


class Department(models.Model):
    objects = None
    name = models.CharField(max_length=100, blank=False)
    creation_date = models.DateField(verbose_name='Дата создания департамента', blank=False)

    def __str__(self):
        """Выводим название"""
        return self.name


class Worker(models.Model):
    objects = None
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0, db_default=0)

    """
    def __str__(self):
        """"""Выводим фамилию""""""
        return self.surname"""

    def __str__(self):
        """Выводим и имя, и фамилию"""
        return f'{self.surname} {self.name} {self.department} {self.salary}'


class Country(models.Model):
    objects = None
    name = models.CharField(max_length=100, blank=False)
    
    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'{self.name}'
