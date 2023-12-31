# Generated by Django 4.2.4 on 2023-08-04 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('birds', '0002_alter_birds_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirdsSeen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('number_vision_acts', models.IntegerField(default=1, verbose_name='Количество актов видения')),
                ('birds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birds_seen', to='birds.birds', verbose_name='Увиденные птицы')),
            ],
        ),
    ]
