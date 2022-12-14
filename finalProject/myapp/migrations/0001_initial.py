# Generated by Django 4.1.4 on 2022-12-13 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name of brand')),
                ('img', models.CharField(max_length=255, verbose_name='Photo of brand')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorName', models.CharField(max_length=255, verbose_name='Color name ')),
                ('color', models.CharField(max_length=255, verbose_name='Code of the color ')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopName', models.CharField(max_length=255, verbose_name='Name of Shop')),
                ('shopCount', models.CharField(max_length=255, verbose_name='How many product are there ?')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255, verbose_name='размер')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('img', models.CharField(max_length=255, verbose_name='Photo of product')),
                ('images', models.TextField(verbose_name='All photos')),
                ('sale', models.IntegerField(verbose_name='Sale ')),
                ('newPrice', models.IntegerField(verbose_name='New price ')),
                ('oldPrice', models.IntegerField(verbose_name='Old price (If it is in a sale !!!)')),
                ('article', models.CharField(max_length=255, verbose_name='Article of product')),
                ('isNew', models.BooleanField(default=True, verbose_name='New')),
                ('isStar', models.BooleanField(default=False, verbose_name='Star')),
                ('isPOpular', models.BooleanField(default=False, verbose_name='Popular')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.brand', verbose_name='Which brand')),
                ('color', models.ManyToManyField(to='myapp.color', verbose_name='цвет')),
                ('shop', models.ManyToManyField(to='myapp.shop', verbose_name='Shop')),
                ('size', models.ManyToManyField(to='myapp.size', verbose_name='размер')),
            ],
        ),
    ]
