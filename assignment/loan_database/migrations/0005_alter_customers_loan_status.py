# Generated by Django 5.0.3 on 2024-03-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0004_alter_customers_loan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='loan_status',
            field=models.CharField(max_length=20),
        ),
    ]