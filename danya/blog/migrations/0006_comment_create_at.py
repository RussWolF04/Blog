# Generated by Django 4.0 on 2021-12-27 23:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
