# Generated by Django 5.0.5 on 2024-05-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]
