# Generated by Django 4.2.2 on 2023-06-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_mostplayed'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostPlayed_object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='image')),
                ('category', models.CharField(max_length=30, verbose_name='Category ')),
                ('name', models.CharField(max_length=30, verbose_name=' name')),
                ('button_name', models.CharField(max_length=60, verbose_name='Button Name')),
            ],
        ),
    ]
