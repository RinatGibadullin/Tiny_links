# Generated by Django 3.0.5 on 2020-05-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_link_follow_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tiny_link',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
