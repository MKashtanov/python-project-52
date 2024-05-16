# Generated by Django 4.2.5 on 2023-10-24 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_remove_task_label_task_labels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_performer',
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='executor',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Executor'),
            preserve_default=False,
        ),
    ]
