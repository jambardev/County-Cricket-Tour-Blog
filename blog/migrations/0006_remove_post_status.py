# Generated by Django 4.2.13 on 2024-07-16 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_competition_alter_post_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
