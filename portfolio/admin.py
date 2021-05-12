from django.contrib import admin
from .models import Contact
# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'message_date' ,'name', 'email' , 'subject' , 'message']
admin.site.register(Contact , AdminContact)
