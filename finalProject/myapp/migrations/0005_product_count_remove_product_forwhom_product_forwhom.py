# Generated by Django 4.1.4 on 2022-12-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_merge_20221213_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default='5', verbose_name='Count'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='forWhom',
        ),
        migrations.AddField(
            model_name='product',
            name='forWhom',
            field=models.CharField(choices=[('MEN', 'MEN'), ('WOMEN', 'WOMEN'), ('CHILDREN', 'CHILDREN')], default=(('MEN', 'MEN'), ('WOMEN', 'WOMEN'), ('CHILDREN', 'CHILDREN')), max_length=10),
        ),
    ]