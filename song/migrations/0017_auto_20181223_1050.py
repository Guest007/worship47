# Generated by Django 2.0.6 on 2018-12-23 07:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0016_auto_20181211_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='accords',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='presentation',
            field=models.FileField(blank=True, upload_to='presentations/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='text_eng',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
