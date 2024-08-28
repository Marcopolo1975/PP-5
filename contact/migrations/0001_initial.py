# Generated by Django 3.2.25 on 2024-08-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('enquiry_type', models.CharField(choices=[('PRODUCT_QUERY', 'Product Query'), ('SHIPPING_QUERY', 'Shipping Query'), ('ORDER_QUERY', 'Order Query'), ('OTHER', 'Other')], default='DS', max_length=254)),
                ('message', models.TextField(default='', max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
