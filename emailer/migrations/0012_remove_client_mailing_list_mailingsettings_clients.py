# Generated by Django 4.2.3 on 2023-08-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0011_alter_client_mailing_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mailing_list',
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='clients',
            field=models.ManyToManyField(to='emailer.client', verbose_name='клиенты'),
        ),
    ]
