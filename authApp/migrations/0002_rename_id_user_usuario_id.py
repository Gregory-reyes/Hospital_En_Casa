# Generated by Django 4.1.1 on 2022-09-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='id_user',
            new_name='id',
        ),
    ]