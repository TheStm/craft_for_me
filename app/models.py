from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    role = models.CharField(max_length=100, default='basic_users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class Owner(User):
    shop_name = models.CharField(max_length=100)

class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    coordinates = models.OneToOneField('Coordinates', on_delete=models.CASCADE)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        coord_str = f"Latitude: {self.latitude}, Longitude: {self.longitude}"
        return coord_str

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review