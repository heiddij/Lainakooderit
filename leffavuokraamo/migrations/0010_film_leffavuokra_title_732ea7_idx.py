# Generated by Django 4.1.1 on 2022-10-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leffavuokraamo', '0009_alter_rental_date_returned'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='film',
            index=models.Index(fields=['title'], name='leffavuokra_title_732ea7_idx'),
        ),
    ]
