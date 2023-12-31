# Generated by Django 4.2.6 on 2023-10-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('fecha_de_entrega', models.DateField(verbose_name='fecha de entrega')),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('profesion', models.CharField(max_length=50, verbose_name='profesion')),
            ],
        ),
    ]
