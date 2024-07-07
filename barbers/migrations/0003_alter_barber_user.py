from django.db import migrations, models

def populate_user(apps, schema_editor):
    Barber = apps.get_model('barbers', 'Barber')
    User = apps.get_model('auth', 'User')

    barbers_without_user = Barber.objects.filter(user=None)

    for barber in barbers_without_user:
        user = User.objects.exclude(barber__isnull=False).first()
        if user:
            barber.user = user
            barber.save()

class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0002_barber_user'),
    ]

    operations = [
        migrations.RunPython(populate_user, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='barber',
            name='user',
            field=models.OneToOneField(
                on_delete=models.CASCADE,
                to='auth.User',
            ),
            preserve_default=False,
        ),
    ]
