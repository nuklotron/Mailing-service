# Generated by Django 4.2.3 on 2023-08-28 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0007_remove_client_mailing_list_client_mailing_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglog',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailer.message', verbose_name='подписка клиента'),
        ),
    ]
