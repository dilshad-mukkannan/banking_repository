# Generated by Django 3.1.7 on 2023-11-07 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0008_auto_20231107_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.ForeignKey(limit_choices_to={'district.primary_key': False}, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='bank_app.branch'),
        ),
    ]
