# Generated by Django 4.0.4 on 2022-06-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0017_usuario_groups_usuario_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]