# Generated by Django 3.1.1 on 2020-09-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_post_categorey'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categorey',
            field=models.TextField(default=None, null=True),
        ),
    ]