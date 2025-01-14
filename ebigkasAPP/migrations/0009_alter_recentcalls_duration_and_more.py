# Generated by Django 5.1 on 2024-09-02 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebigkasAPP', '0008_alter_recentcalls_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentcalls',
            name='duration',
            field=models.DurationField(blank=True, default=datetime.timedelta(0), null=True),
        ),
        migrations.AlterField(
            model_name='recentcalls',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
