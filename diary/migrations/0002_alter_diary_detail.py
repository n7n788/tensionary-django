# Generated by Django 4.0.2 on 2022-02-25 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='detail',
            field=models.CharField(max_length=500),
        ),
    ]
