# Generated by Django 3.0.10 on 2024-08-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year_built', models.IntegerField(default=2024)),
                ('color', models.CharField(max_length=64)),
                ('horsepower', models.IntegerField()),
            ],
        ),
    ]