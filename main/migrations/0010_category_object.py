# Generated by Django 4.2.2 on 2023-06-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=' name')),
                ('img', models.ImageField(upload_to='images', verbose_name='image')),
            ],
        ),
    ]
