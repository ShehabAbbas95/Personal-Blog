# Generated by Django 3.1.1 on 2020-10-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20201001_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='year_in_school',
            field=models.CharField(choices=[], default='x', max_length=2),
        ),
    ]