# Generated by Django 5.0.4 on 2024-05-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_schoolmanagementschools'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolmanagementschools',
            name='id',
        ),
        migrations.AddField(
            model_name='schoolmanagementschools',
            name='schoolmgtschoolID',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
