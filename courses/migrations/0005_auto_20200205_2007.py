# Generated by Django 3.0.2 on 2020-02-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200205_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='date_enroll',
            field=models.DateField(auto_now_add=True),
        ),
    ]