# Generated by Django 5.0.3 on 2024-03-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='lang',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
