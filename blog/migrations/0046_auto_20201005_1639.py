# Generated by Django 3.1.1 on 2020-10-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_auto_20201005_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ManyToManyField(blank=True, to='blog.Categoreies'),
        ),
    ]