# Generated by Django 3.0.4 on 2020-04-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_enproduct_ruproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enproduct',
            name='discount',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='ruproduct',
            name='discount',
            field=models.IntegerField(default=None),
        ),
    ]