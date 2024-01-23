from django.db import models

class Category(models.Model):
    productname = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self) -> str:
        return self.productname
    
class Product(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    price = models.CharField(max_length=40,null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    purchases = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name