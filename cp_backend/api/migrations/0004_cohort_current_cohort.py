# Generated by Django 3.1.1 on 2020-09-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200904_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohort',
            name='current_cohort',
            field=models.BooleanField(default=False),
        ),
    ]