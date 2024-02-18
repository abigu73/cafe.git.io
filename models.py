from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=40)
    image = models.ImageField(upload_to='product_images/') 



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
    

    def __str__(self):
        return f"{self.name} ({self.id})"
