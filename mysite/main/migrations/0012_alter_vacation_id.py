# Generated by Django 4.2.1 on 2023-05-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='ID',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
