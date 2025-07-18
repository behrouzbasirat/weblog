# Generated by Django 4.2.20 on 2025-06-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
