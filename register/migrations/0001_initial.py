# Generated by Django 5.1.3 on 2024-12-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Password2', models.CharField(max_length=200)),
            ],
        ),
    ]
