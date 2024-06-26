from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
