# Generated by Django 3.2.7 on 2021-09-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='location/'),
        ),
    ]
