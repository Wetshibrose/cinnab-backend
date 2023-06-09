# Generated by Django 4.1.7 on 2023-04-07 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_alter_currency_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0001_initial'),
        ('payment_methods', '0001_initial'),
        ('theme', '0001_initial'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_notified', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencies.currency')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='languages.language')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment_methods.paymentmethod')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='theme.theme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]
