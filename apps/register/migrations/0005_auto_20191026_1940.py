# Generated by Django 2.2.1 on 2019-10-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20191026_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='workplace',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='location',
        ),
        migrations.RemoveField(
            model_name='diseases',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='workplace',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='workplace',
        ),
        migrations.AddField(
            model_name='doctor',
            name='field',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]
