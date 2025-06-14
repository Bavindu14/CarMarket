from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vehicle, Bid

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'starting_price', 'owner', 'created_at')
    search_fields = ('make', 'model')
    list_filter = ('make', 'year')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'bidder', 'max_price', 'created_at')
    search_fields = ('vehicle__make', 'vehicle__model')
    list_filter = ('created_at',)