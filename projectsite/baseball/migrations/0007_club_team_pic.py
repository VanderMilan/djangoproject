# Generated by Django 3.2.16 on 2022-11-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0006_auto_20221126_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='team_pic',
            field=models.ImageField(blank=True, default='defaultimg.png', null=True, upload_to='', verbose_name='Team Image'),
        ),
    ]