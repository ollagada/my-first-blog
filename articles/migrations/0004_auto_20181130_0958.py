# Generated by Django 2.1.3 on 2018-11-30 00:58

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20181130_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=sorl.thumbnail.fields.ImageField(default='no_image.png', upload_to='thumbnails'),
        ),
    ]
