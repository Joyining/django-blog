# Generated by Django 4.1.7 on 2023-04-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]
