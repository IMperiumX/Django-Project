# Generated by Django 5.0.1 on 2024-02-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]