from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Shop)
admin.site.register(Review)

