# Generated by Django 4.1.7 on 2023-04-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_category_meta_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='related_categories',
            field=models.ManyToManyField(blank=True, to='categories.category'),
        ),
    ]
