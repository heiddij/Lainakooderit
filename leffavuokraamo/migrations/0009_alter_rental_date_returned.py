# Generated by Django 4.1.1 on 2022-10-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leffavuokraamo', '0008_rename_return_date_rental_last_return_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='date_returned',
            field=models.DateField(null=True),
        ),
    ]