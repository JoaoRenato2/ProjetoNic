# Generated by Django 4.0.4 on 2022-06-16 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0014_alter_usuario_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
    ]