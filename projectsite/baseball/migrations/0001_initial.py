# Generated by Django 3.2.16 on 2022-11-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('height', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('weight', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
            ],
        ),
    ]
