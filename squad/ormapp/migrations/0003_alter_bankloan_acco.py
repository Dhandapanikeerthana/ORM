# Generated by Django 5.1.2 on 2024-10-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0002_alter_bankloan_acco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankloan',
            name='acco',
            field=models.IntegerField(max_length=30, primary_key='acco', serialize=False),
        ),
    ]
