# Generated by Django 2.2.3 on 2019-07-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190731_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
