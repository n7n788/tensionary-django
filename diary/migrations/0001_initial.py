# Generated by Django 4.0.2 on 2022-02-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tension', models.IntegerField()),
                ('detail', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.user')),
            ],
        ),
    ]
