# Generated by Django 5.0.6 on 2024-06-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_intent_id',
            field=models.CharField(default='temporary', max_length=255),
        ),
    ]