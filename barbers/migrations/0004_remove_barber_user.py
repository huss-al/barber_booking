# Generated by Django 4.2.13 on 2024-07-09 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0003_alter_barber_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='user',
        ),
    ]
