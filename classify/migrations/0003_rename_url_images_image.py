# Generated by Django 4.0.3 on 2022-03-16 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0002_remove_images_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='url',
            new_name='image',
        ),
    ]
