# Generated by Django 4.0.3 on 2022-03-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
