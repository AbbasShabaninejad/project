# Generated by Django 5.0.4 on 2024-05-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]