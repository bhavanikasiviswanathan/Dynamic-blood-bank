from django.contrib import admin

# Register your models here.
from .models import Bloodbank, Donor, User

admin.site.register(Bloodbank)
admin.site.register(Donor)
admin.site.register(User)
