# Generated by Django 4.0.4 on 2022-05-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_categories_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
    ]
