# Generated by Django 4.0.4 on 2022-06-06 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0010_rename_agendamentos_consultas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='senha',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='username',
        ),
        migrations.AddField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
