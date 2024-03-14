from django.contrib import admin

# Register your models here.
from .models import Customers,Admin
admin.site.register(Admin)
admin.site.register(Customers)