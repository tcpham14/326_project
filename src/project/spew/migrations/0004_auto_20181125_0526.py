# Generated by Django 2.1.2 on 2018-11-25 05:26

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('spew', '0003_auto_20181122_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spewuser',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='spewuser',
            name='password2',
        ),
    ]