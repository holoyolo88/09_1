# Generated by Django 2.1.1 on 2018-09-28 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeroNine', '0003_auto_20180919_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img_path',
        ),
    ]
