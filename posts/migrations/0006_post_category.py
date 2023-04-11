# Generated by Django 4.1.7 on 2023-04-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'General'), (1, 'DevOps'), (2, 'Web3'), (3, 'Life')], default=0),
        ),
    ]
