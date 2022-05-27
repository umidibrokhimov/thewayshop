# Generated by Django 4.0.4 on 2022-05-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog posts',
            },
        ),
        migrations.CreateModel(
            name='HomeCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Home Categories',
            },
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=20)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('fb_account', models.URLField(blank=True, max_length=10, null=True)),
                ('tr_account', models.URLField(blank=True, max_length=10, null=True)),
                ('gl_account', models.URLField(blank=True, max_length=10, null=True)),
                ('yt_account', models.URLField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]