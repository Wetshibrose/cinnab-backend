# Generated by Django 4.1.7 on 2023-04-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('businesses', '0001_initial'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='business',
            field=models.ManyToManyField(blank=True, to='businesses.business'),
        ),
        migrations.AddIndex(
            model_name='brandlogo',
            index=models.Index(fields=['id', 'is_deleted'], name='brands_bran_id_a85557_idx'),
        ),
        migrations.AddIndex(
            model_name='brand',
            index=models.Index(fields=['id', 'name'], name='brands_bran_id_0fae9e_idx'),
        ),
    ]
