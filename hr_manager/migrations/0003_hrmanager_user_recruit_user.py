# Generated by Django 4.2.7 on 2023-11-14 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_manager', '0002_recruit_report_recruittraining_recruitperformance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrmanager',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recruit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
