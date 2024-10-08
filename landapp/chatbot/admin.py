from django.contrib import admin
from .models import Complain, Category


admin.site.register(Category)
admin.site.register(Complain)
