# Generated by Django 5.0.6 on 2024-05-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default=4, max_length=255),
            preserve_default=False,
        ),
    ]