# Generated by Django 4.0.2 on 2023-07-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathematics', '0003_alter_exercise_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
