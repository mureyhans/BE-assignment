from django.db import models


# Create your models here.
class Contact(models.Model):
    phone_num = models.CharField(max_length=15, blank=False, null=False)
    name = models.CharField(max_length=60, blank=True, default=phone_num)
    email_address = models.EmailField(max_length=320, blank=True, default='')

    def __str__(self):
        return self.name


class ContactList(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    contacts = models.ManyToManyField(Contact, related_name='contact_list', blank=True)

    def __str__(self):
        return self.name
