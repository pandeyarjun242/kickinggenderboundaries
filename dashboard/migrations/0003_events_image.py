# Generated by Django 2.2.8 on 2020-01-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
