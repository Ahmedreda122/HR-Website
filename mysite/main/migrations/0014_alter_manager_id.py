# Generated by Django 4.2.1 on 2023-06-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20230601_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
