# Generated by Django 4.1.7 on 2023-04-21 07:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'ordering': ['name'],
                'permissions': (('can_view_brand', 'Can view brand'), ('can_add_brand', 'Can add brand'), ('can_edit_brand', 'Can edit brand'), ('can_delete_brand', 'Can delete brand')),
                'default_related_name': 'brands',
            },
        ),
        migrations.CreateModel(
            name='BrandLogo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(blank=True, null=True, verbose_name='url image')),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='brands.brand')),
            ],
            options={
                'verbose_name': 'brand logo',
                'verbose_name_plural': 'brand logos',
                'ordering': ['-date_created'],
                'default_related_name': 'brandlogos',
            },
        ),
    ]
