# Generated by Django 3.2 on 2022-08-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_started', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Язык программирования')),
                ('months_to_learn', models.IntegerField(verbose_name='Длительность(месяц)')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронка')),
                ('phone_number', models.CharField(max_length=25, verbose_name='Номер телефона')),
                ('work_study_place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место работы/учебы')),
                ('has_own_notebook', models.BooleanField(verbose_name='Наличие ноутбука')),
                ('preferred_os', models.CharField(choices=[('windows', 'Windows'), ('macos', 'MacOS'), ('linux', 'Linux')], max_length=50, verbose_name='ОС')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронка')),
                ('phone_number', models.CharField(max_length=25, verbose_name='Номер телефона')),
                ('main_work', models.CharField(blank=True, max_length=50, null=True, verbose_name='место работы')),
                ('experience', models.DateField(verbose_name='Начало работы')),
                ('students', models.ManyToManyField(through='user.Course', to='user.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.language'),
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]
