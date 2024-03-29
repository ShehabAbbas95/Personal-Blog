# Generated by Django 3.1.1 on 2020-10-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshasdasmans'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshasdasmans'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
