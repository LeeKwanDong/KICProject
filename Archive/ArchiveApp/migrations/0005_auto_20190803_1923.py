# Generated by Django 2.2.3 on 2019-08-03 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArchiveApp', '0004_auto_20190727_2351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'managed': False, 'ordering': ('-idx',)},
        ),
    ]
