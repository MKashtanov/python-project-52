# Generated by Django 4.2.5 on 2023-10-23 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_label_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'Label', 'verbose_name_plural': 'Метки'},
        ),
    ]