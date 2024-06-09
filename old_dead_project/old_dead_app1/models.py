from django.db import models


class Department(models.Model):
    objects = None
    name = models.CharField(max_length=100, blank=False)
    creation_date = models.DateField(verbose_name='Дата создания департамента', blank=False)

    def __str__(self):
        """Выводим название"""
        return f'{self.name}'


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
    flag = models.ImageField(upload_to='flags/', blank=False)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'{self.name} ({self.flag.url})'


class Currency(models.Model):
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='currencies', blank=False)
    abbreviation = models.CharField(max_length=3, blank=False, unique=True)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return f'{self.name} {self.abbreviation} ({self.image.url})'


class ScienceDegree(models.Model):
    objects = None
    name = models.CharField(max_length=50, blank=False)
    parent_degree = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class TeachingDegree(models.Model):
    objects = None
    name = models.CharField(max_length=50, blank=False)
    parent_degree = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    # Определение полей модели
    name = models.CharField(max_length=40, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    subjects = models.ManyToManyField('Subject', related_name='teachers')
    citizenship = models.ForeignKey(Country, on_delete=models.CASCADE)
    science_degree = models.ForeignKey('ScienceDegree', blank=False, on_delete=models.CASCADE)
    teaching_degree = models.ForeignKey('TeachingDegree', blank=False, on_delete=models.CASCADE)
    external_teacher = models.BooleanField(default=False)
    salary = models.IntegerField(blank=False, null=False, serialize=True)
    currency_abbreviation = models.ForeignKey('Currency', to_field='abbreviation',
                                              blank=False, on_delete=models.PROTECT)
    capacity = models.IntegerField(verbose_name='Capacity in hours per week')

    def __str__(self):
        return (
                f'{self.name} {self.surname} {self.citizenship} {self.science_degree}'
                f'{self.teaching_degree} {self.external_teacher} {self.salary}'
                f'{self.currency_abbreviation} {self.capacity}'
                )


class Student(models.Model):
    objects = None
    name = models.CharField(max_length=40, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    subjects = models.ManyToManyField('Subject', related_name='students')
    citizenship = models.ForeignKey(Country, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', to_field='speciality', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname} {self.citizenship} {self.group}'


class Group(models.Model):
    objects = None
    number = models.IntegerField(unique=True, blank=False)
    speciality = models.CharField(max_length=50, blank=False)
    head = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} {self.speciality} {self.head} {Subject.name}'


class Subject(models.Model):
    objects = None
    name = models.CharField(max_length=150, blank=False)
    teachers = models.ManyToManyField('Teacher', related_name='subjects')
    groups = models.ManyToManyField('Group', related_name='subjects')

    def __str__(self):
        return f'{self.name} {self.teachers} {self.groups}'


class HoursNumber(models.Model):
    objects = None
    group = models.ForeignKey('Group', to_field='number', blank=False, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', to_field='name', blank=False, on_delete=models.CASCADE)
    number_of_hours = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.group} {self.subject} {self.number_of_hours}'
