# Generated by Django 2.2.3 on 2019-07-27 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArchiveApp', '0002_moviereview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'managed': False, 'ordering': ('-idx',)},
        ),
    ]