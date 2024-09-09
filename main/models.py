from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    pairing = models.TextField()
    date = models.DateField(auto_now_add=True)

    @property
    def is_this_good(self):
        return self.rating > 4