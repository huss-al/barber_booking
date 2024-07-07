# Generated by Django 4.2.13 on 2024-07-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
            ],
        ),
    ]
