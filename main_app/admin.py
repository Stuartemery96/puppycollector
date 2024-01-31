from django.contrib import admin
from .models import Puppy, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Puppy)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)