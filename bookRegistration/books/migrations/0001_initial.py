# Generated by Django 5.0.6 on 2024-07-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
    ]
