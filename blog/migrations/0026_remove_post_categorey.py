# Generated by Django 3.1.1 on 2020-09-27 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post_categorey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categorey',
        ),
    ]
