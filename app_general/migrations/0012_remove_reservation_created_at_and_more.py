# Generated by Django 4.2.5 on 2023-10-28 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0011_remove_orders_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='total_price',
        ),
        migrations.AddField(
            model_name='orders',
            name='total_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_general.customer'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]