# Generated by Django 2.0.13 on 2019-12-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentsInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videodatetime', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
                ('video_name', models.CharField(blank=True, max_length=100)),
                ('video_path', models.CharField(default='/', max_length=200, null=True)),
                ('check', models.IntegerField()),
            ],
        ),
    ]
