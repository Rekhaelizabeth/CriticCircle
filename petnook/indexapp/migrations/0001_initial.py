# Generated by Django 4.2.5 on 2023-09-28 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=None, max_length=100, null=True)),
                ('pet_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.petcategory')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('addressline1', models.CharField(max_length=100)),
                ('addressline2', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(default=None, max_length=100, null=True)),
                ('pet_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.petcategory')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='indexapp.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('brand_name', models.CharField(blank=True, max_length=255, null=True)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('num_items', models.PositiveIntegerField()),
                ('quantity_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('priceUnit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image1', models.ImageField(upload_to='product_images/')),
                ('image2', models.ImageField(upload_to='product_images/')),
                ('image3', models.ImageField(upload_to='product_images/')),
                ('pet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.petcategory')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.productcategory')),
                ('product_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.productsubcategory')),
            ],
        ),
    ]
