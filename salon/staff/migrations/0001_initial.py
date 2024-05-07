# Generated by Django 5.0.3 on 2024-03-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('skills', models.TextField()),
                ('picture', models.ImageField(upload_to=None)),
            ],
        ),
    ]
