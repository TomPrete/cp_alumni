# Generated by Django 3.1.1 on 2020-12-02 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200925_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cohort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cohorts', to='api.cohort'),
        ),
    ]
