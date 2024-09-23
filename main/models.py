import uuid
from django.db import models
from django.contrib.auth.models import User

class AdornmentsEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()

    @property
    def low_stock(self):
        return self.quantity < 5