from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    zipcode = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"