# Generated by Django 5.1.6 on 2025-02-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0004_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
