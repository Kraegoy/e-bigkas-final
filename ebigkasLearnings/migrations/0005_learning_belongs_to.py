# Generated by Django 5.1.1 on 2024-10-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebigkasLearnings', '0004_userlearning'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='belongs_to',
            field=models.TextField(default=''),
        ),
    ]
