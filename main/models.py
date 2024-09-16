from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    pairing = models.TextField()
    date = models.DateField(auto_now_add=True)

    @property
    def is_this_good(self):
        return self.rating > 4 