# Generated by Django 5.1.4 on 2024-12-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_assignment_type_alter_assignment_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='coder_email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
