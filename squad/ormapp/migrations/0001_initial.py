# Generated by Django 5.1.2 on 2024-10-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('acco', models.IntegerField(max_length=30, primary_key='acco', serialize=False)),
                ('age', models.IntegerField()),
                ('emiinterest', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('pancard', models.IntegerField()),
                ('mobileno', models.IntegerField()),
            ],
        ),
    ]
