from django.contrib import admin
from .models import Contact, ContactList

# Register your models here.
admin.site.register(Contact)
admin.site.register(ContactList)
# admin.site.register(ContactListDetail)