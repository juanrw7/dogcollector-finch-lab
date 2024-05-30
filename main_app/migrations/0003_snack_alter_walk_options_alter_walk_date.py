# Generated by Django 4.2.13 on 2024-05-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_walk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='walk',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='walk',
            name='date',
            field=models.DateField(verbose_name='Date of the Walk'),
        ),
    ]
