# Generated by Django 3.0.6 on 2020-06-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArchiveApp', '0005_auto_20190803_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pwd', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
    ]
