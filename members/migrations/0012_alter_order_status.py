# Generated by Django 4.0.5 on 2022-07-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_profile_email_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping')], default='Pending', max_length=150),
        ),
    ]