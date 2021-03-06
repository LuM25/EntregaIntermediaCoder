# Generated by Django 4.0.4 on 2022-06-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receta_1a3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ingrediente_1', models.FloatField()),
                ('ingrediente_2', models.FloatField()),
                ('ingrediente_3', models.FloatField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='receta_3a6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ingrediente_1', models.FloatField()),
                ('ingrediente_2', models.FloatField()),
                ('ingrediente_3', models.FloatField()),
                ('ingrediente_4', models.FloatField()),
                ('ingrediente_5', models.FloatField()),
                ('ingrediente_6', models.FloatField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='receta_6a10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ingrediente_1', models.FloatField()),
                ('ingrediente_2', models.FloatField()),
                ('ingrediente_3', models.FloatField()),
                ('ingrediente_4', models.FloatField()),
                ('ingrediente_5', models.FloatField()),
                ('ingrediente_6', models.FloatField()),
                ('ingrediente_7', models.FloatField()),
                ('ingrediente_8', models.FloatField()),
                ('ingrediente_9', models.FloatField()),
                ('ingrediente_10', models.FloatField()),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
    ]
