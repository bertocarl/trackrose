# Generated by Django 2.2.6 on 2019-10-15 09:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('e_mail', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('Image', models.ImageField(upload_to='static/profile/')),
                ('address', models.CharField(max_length=128)),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('ID', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('Image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.User')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('inout', models.NullBooleanField(verbose_name='inout')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.User')),
            ],
            options={
                'unique_together': {('task', 'user')},
            },
        ),
    ]
