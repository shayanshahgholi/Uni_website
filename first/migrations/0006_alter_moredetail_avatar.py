# Generated by Django 4.0.6 on 2022-08-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_alter_moredetail_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moredetail',
            name='avatar',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
