# Generated by Django 3.0.4 on 2020-04-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_rublog'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('price_sale', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RuProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('price_sale', models.FloatField()),
            ],
        ),
    ]
