from django.contrib import admin
from .models import RF_Services,AC_Services,WM_Services, Users
# Register your models here.

admin.site.register(RF_Services)
admin.site.register(AC_Services)
admin.site.register(WM_Services)
admin.site.register(Users)