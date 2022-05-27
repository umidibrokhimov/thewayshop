# Generated by Django 4.0.4 on 2022-05-27 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_products_is_new_products_is_sale'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductCategories',
        ),
        migrations.AddField(
            model_name='products',
            name='brand_clothe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.brandcategories'),
        ),
        migrations.AddField(
            model_name='products',
            name='type_clothe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.categories'),
        ),
    ]