# Generated by Django 3.0.4 on 2020-04-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=64)),
                ('date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='Admin', max_length=30)),
                ('head_text', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]