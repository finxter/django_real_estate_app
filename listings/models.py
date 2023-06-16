from django.db import models

# Create your models here.

class Listing(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    n_bedrooms = models.IntegerField(null=True)
    n_bathrooms = models.IntegerField(null=True)
    sqft = models.IntegerField()
    image = models.ImageField(upload_to='images')
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name







#from django.db import models
#from django.contrib.auth.models import User

#class Contact(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    email = models.EmailField()
#    subject = models.CharField(max_length=255)
#    message = models.TextField()

#    def __str__(self):
#        return self.email

