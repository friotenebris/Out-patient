# Generated by Django 2.2.1 on 2019-10-27 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20191026_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseases',
            name='username',
        ),
        migrations.AddField(
            model_name='diseases',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
