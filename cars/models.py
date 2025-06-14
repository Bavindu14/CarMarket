from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)  # Allow null for no image
    mileage = models.PositiveIntegerField(help_text="Mileage in kilometers", null=True, blank=True)
    condition = models.CharField(max_length=50, choices=[('New', 'New'), ('Used', 'Used'), ('Certified Pre-Owned', 'Certified Pre-Owned')], default='Used')
    transmission = models.CharField(max_length=50, choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Automatic')
    owner_phone = models.CharField(max_length=15, null=True, blank=True, help_text="Owner's contact phone number")
    owner_email = models.EmailField(max_length=254, null=True, blank=True, help_text="Owner's contact email")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.vehicle} - {self.uploaded_at}"

class Bid(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid of ${self.max_price} on {self.vehicle}"