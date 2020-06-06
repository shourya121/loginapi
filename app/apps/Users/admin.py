from django.contrib import admin

# Register your models here.
#admin.site.register(custom_user)
from Users.models import custom_user
admin.site.register(custom_user)
