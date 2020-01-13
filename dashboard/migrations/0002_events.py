# Generated by Django 2.2.8 on 2020-01-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField()),
                ('past_events', models.IntegerField()),
            ],
        ),
    ]
