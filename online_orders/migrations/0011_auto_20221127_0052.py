# Generated by Django 3.2.7 on 2022-11-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_orders', '0010_auto_20221123_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryimageattachment',
            name='file',
            field=models.FileField(upload_to='product\\primaryImages'),
        ),
        migrations.AlterField(
            model_name='secondaryimageattachment',
            name='file',
            field=models.FileField(upload_to='product\\secondaryImages'),
        ),
    ]
