# Generated by Django 5.1.1 on 2024-10-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Email', models.CharField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
