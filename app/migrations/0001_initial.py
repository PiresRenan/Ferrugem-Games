# Generated by Django 4.1.3 on 2022-11-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('phone', models.IntegerField()),
                ('mensagem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=125, null=True)),
                ('dt_nasc', models.DateField()),
                ('email', models.CharField(max_length=125)),
                ('cidade', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]
