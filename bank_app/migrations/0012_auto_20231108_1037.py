# Generated by Django 3.1.7 on 2023-11-08 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0011_auto_20231108_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.branch'),
        ),
    ]
