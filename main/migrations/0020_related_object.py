# Generated by Django 4.2.2 on 2023-06-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_related'),
    ]

    operations = [
        migrations.CreateModel(
            name='Related_object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='imge')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
        ),
    ]
