from django.contrib import admin
# import your models here
from .models import Dog, Walk, Snack

# Register your models here
admin.site.register(Dog)
admin.site.register(Walk)
admin.site.register(Snack)