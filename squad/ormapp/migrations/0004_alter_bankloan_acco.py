# Generated by Django 5.1.2 on 2024-10-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0003_alter_bankloan_acco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankloan',
            name='acco',
            field=models.IntegerField(primary_key='True', serialize=False),
        ),
    ]
