# Generated by Django 4.1.5 on 2023-01-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='chegada_ao_brasil',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_casamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]