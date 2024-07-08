# Generated by Django 4.2.13 on 2024-07-07 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barbers', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('datetime', models.DateTimeField()),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='barbers.barber')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='profiles.profile')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='appointments.cuttype')),
            ],
            options={
                'unique_together': {('datetime', 'barber')},
            },
        ),
    ]