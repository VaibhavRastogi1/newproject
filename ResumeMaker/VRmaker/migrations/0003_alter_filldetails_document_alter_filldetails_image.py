# Generated by Django 4.1.4 on 2023-01-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRmaker', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filldetails',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='mydocument'),
        ),
        migrations.AlterField(
            model_name='filldetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='myimage'),
        ),
    ]