# Generated by Django 2.1.5 on 2020-08-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200829_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscomment',
            name='post_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userscomment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]