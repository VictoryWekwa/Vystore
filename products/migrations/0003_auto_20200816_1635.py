# Generated by Django 2.2 on 2020-08-16 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200816_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='name',
            new_name='product',
        ),
    ]
