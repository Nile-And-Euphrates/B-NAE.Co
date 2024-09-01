from django.db import models

# Create your models here.


class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photo/', null=True, blank=True)
    description=models.TextField(max_length=800, blank=True)
    price=models.IntegerField(default=0)
    discount=models.BooleanField(default=False)
    discountAmount=models.IntegerField(default=0)
    category = models.CharField(max_length=49 , default = "")
        
    def __str__(self):
        return self.name
