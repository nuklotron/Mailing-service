# Generated by Django 4.2.3 on 2023-08-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0002_client_mailing_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingsettings',
            name='message',
            field=models.ManyToManyField(to='emailer.message', verbose_name='рассылка'),
        ),
    ]
