# Generated by Django 4.0.4 on 2022-05-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
