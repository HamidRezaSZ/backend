# Generated by Django 4.0.3 on 2022-03-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='title',
        ),
    ]