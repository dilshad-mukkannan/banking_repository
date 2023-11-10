# Generated by Django 3.1.7 on 2023-11-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0019_auto_20231108_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='materials_provided',
            field=models.CharField(choices=[('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('Cheque Book', 'Cheque Book')], default='your card', max_length=250),
        ),
    ]