# Generated by Django 5.1.4 on 2024-12-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_alter_studentmaster_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmaster',
            name='code',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]