from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык программирования')
    months_to_learn = models.IntegerField(verbose_name='Длительность(месяц)')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронка')
    phone_number = models.CharField(max_length=25, verbose_name='Номер телефона')

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     if self.phone_number[0] == '0':
    #         self.phone_number = '+996'
    #
    #
    #     super().save(*args, **kwargs)


class Student(AbstractPerson):
    os = [('windows', 'Windows'), ('macos', 'MacOS'), ('linux', 'Linux')]
    work_study_place = models.CharField(max_length=100, verbose_name='Место работы/учебы', null=True, blank=True)
    has_own_notebook = models.BooleanField(verbose_name='Наличие ноутбука')
    preferred_os = models.CharField(max_length=50, choices=os, verbose_name='ОС')

    def __str__(self):
        return self.name

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, verbose_name='место работы', null=True, blank=True)
    experience = models.DateField(verbose_name='Начало работы')
    students = models.ManyToManyField(Student, through='Course')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    # def get_and_date(self):
    #     reuslt =










