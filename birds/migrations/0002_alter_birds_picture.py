# Generated by Django 4.2.4 on 2023-08-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birds',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='bird_pictures/'),
        ),
    ]
