# Generated by Django 5.2.2 on 2025-06-12 20:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('up1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='up1.product'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
