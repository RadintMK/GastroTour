from django.db import models

class Restaurant(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    country = models.CharField(max_length=100)
    rating = models.FloatField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    session_id = models.CharField(max_length=255, default='')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)