# Generated by Django 3.0.3 on 2020-05-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('uuid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('job_titles', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('posted_by', models.CharField(max_length=100)),
                ('date_opened', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField()),
            ],
        ),
    ]
