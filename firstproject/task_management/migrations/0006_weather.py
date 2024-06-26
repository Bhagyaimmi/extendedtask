# Generated by Django 5.0 on 2024-06-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0005_task_status_alter_task_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
