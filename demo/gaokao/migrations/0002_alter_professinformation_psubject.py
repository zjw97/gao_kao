# Generated by Django 3.2.3 on 2021-05-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaokao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professinformation',
            name='psubject',
            field=models.CharField(max_length=100, null=True, verbose_name='学科要求'),
        ),
    ]
