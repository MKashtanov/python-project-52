# Generated by Django 4.2.5 on 2023-10-25 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0013_alter_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(
                blank=True, default='', null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='executor',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Исполнитель'),
        ),
    ]
