# Generated by Django 4.1.1 on 2022-10-07 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuenta',
            old_name='apellido',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cuenta',
            old_name='clave',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='cuenta',
            old_name='nombre',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='cuenta',
            old_name='usuario',
            new_name='username',
        ),
    ]
