# Generated by Django 5.0.4 on 2024-04-28 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_expense_management'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense_management',
            name='category',
        ),
    ]
