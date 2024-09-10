from django.db import models

class AdornmentsEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()

    @property
    def low_stock(self):
        return self.quantity < 5