# Generated by Django 4.2.6 on 2024-03-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classes',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classe',
            field=models.ManyToManyField(to='classes.class'),
        ),
    ]
