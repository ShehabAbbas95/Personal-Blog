# Generated by Django 2.1.5 on 2020-08-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200829_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userscomment',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
