from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','photo','is_mvp','hire_date')
    list_display_links = ('id','name')
    list_per_page= 25
    list_editable = ('is_mvp',)
    search_fields = ('name','email','hire_date')

admin.site.register(Realtor,RealtorAdmin)
