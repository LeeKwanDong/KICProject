# Generated by Django 2.2.3 on 2019-07-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArchiveApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('warning', models.TextField(blank=True, null=True)),
                ('vcategory', models.CharField(blank=True, max_length=20, null=True)),
                ('violence', models.TextField(blank=True, null=True)),
                ('ecategory', models.CharField(blank=True, max_length=20, null=True)),
                ('exposure', models.TextField(blank=True, null=True)),
                ('pcategory', models.CharField(blank=True, max_length=20, null=True)),
                ('profanity', models.TextField(blank=True, null=True)),
                ('dcategory', models.CharField(blank=True, max_length=20, null=True)),
                ('discrimination', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_review',
                'managed': False,
            },
        ),
    ]
