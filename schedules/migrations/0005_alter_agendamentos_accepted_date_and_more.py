# Generated by Django 4.0.4 on 2022-06-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_alter_agendamentos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentos',
            name='accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agendamentos',
            name='observacao',
            field=models.TextField(blank=True),
        ),
    ]