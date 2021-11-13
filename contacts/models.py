from django.db import models


# Create your models here.
class Contact(models.Model):
    phone_num = models.CharField(max_length=15)
    name = models.CharField(max_length=60, blank=True)
    email_address = models.EmailField(max_length=320, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.phone_num
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ContactList(models.Model):
    name = models.CharField(max_length=60)
    contacts = models.ManyToManyField(Contact, related_name='contact_list')

    def __str__(self):
        return self.name
