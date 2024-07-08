from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        
        """
        Returns the url to access a specific product.
        """

        return reverse('app_shop:product_list_by_category', args=[self.slug])
    
class Tag(models.Model):
    
    tag = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.tag)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    
    tag = models.ManyToManyField(
        Tag, related_name='products', blank=True)
    
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True)
    
    
    
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    
    nut_value = models.CharField(max_length=200, blank=True)
    
    netto = models.IntegerField(default=500)
    price = models.IntegerField(default=0)
    
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('app_shop:product_detail',
                       args=[self.id,  self.slug])
