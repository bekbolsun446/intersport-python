from django.db import models


# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name of brand')
    img = models.ImageField(upload_to="brands", verbose_name='Photo of brand')

    def __str__(self):
        return self.title


class ForWhom(models.Model):
    title = models.CharField(max_length=255, verbose_name='For Whom ?')
    img = models.ImageField(upload_to="forWhom", verbose_name='Photo of brand')
    categories = models.ManyToManyField('Category', verbose_name='Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name of category')

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name of Subcategory')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    FOR_WHOM = (
        ("MEN", "MEN"),
        ("WOMEN", "WOMEN"),
        ("CHILDREN", "CHILDREN")
    )
    name = models.CharField(max_length=255, verbose_name='Name of product')
    img = models.CharField(max_length=300, verbose_name='Photo of product')
    images = models.TextField(verbose_name="All photos")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Which brand')
    category = models.ManyToManyField('Category', verbose_name='Category')
    subCategory = models.ManyToManyField('SubCategory', verbose_name='Subcategory')
    sale = models.IntegerField(verbose_name='Sale ')
    newPrice = models.IntegerField(verbose_name='New price ')
    oldPrice = models.IntegerField(verbose_name='Old price (If it is in a sale !!!)')
    # count = models.IntegerField(default="5", verbose_name='Count')
    size = models.ManyToManyField('Size', verbose_name='Size')
    color = models.ManyToManyField('Color', verbose_name='Color')
    article = models.CharField(max_length=255, verbose_name='Article of product')
    shop = models.ManyToManyField('Shop', verbose_name='Shop')
    isNew = models.BooleanField(default=True, verbose_name='New')
    isStar = models.BooleanField(default=False, verbose_name='Star')
    isPopular = models.BooleanField(default=False, verbose_name='Popular')
    forWhom = models.CharField(max_length=10, choices=FOR_WHOM)

    # typeOfSport = models.CharField(max_length=50, verbose_name='Type of sport ')

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=255, verbose_name='размер', )

    def __str__(self):
        return self.size


class Color(models.Model):
    colorName = models.CharField(max_length=255, verbose_name='Color name ')
    color = models.CharField(max_length=255, verbose_name='Code of the color ')

    def __str__(self):
        return self.colorName


class Shop(models.Model):
    shopName = models.CharField(max_length=255, verbose_name='Name of Shop')

    def __str__(self):
        return self.shopName
