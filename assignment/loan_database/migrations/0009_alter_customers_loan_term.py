# Generated by Django 5.0.3 on 2024-03-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_database', '0008_customers_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='loan_term',
            field=models.IntegerField(null=True),
        ),
    ]
