# Generated by Django 4.0 on 2024-01-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0009_brand_category_presentation_product_specification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
