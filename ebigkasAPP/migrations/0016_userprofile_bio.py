# Generated by Django 5.1.1 on 2024-09-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebigkasAPP', '0015_userprofile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
