# Generated by Django 2.2.8 on 2020-01-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eugene', '0002_auto_20200113_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='alpha2code',
            field=models.CharField(max_length=5),
        ),
    ]
