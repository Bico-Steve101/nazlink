# Generated by Django 4.2.2 on 2023-07-06 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['modify', 'created']},
        ),
    ]
