# Generated by Django 3.1.1 on 2020-10-05 14:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20201005_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Coding', 'Coding'), ('ML', 'ML'), ('IOT', 'IOT'), ('Python', 'Python'), ('X', 'X')], default='uncategorized', max_length=22),
        ),
    ]