from rest_framework import serializers
from .models import Contact, ContactList


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = ContactList
        fields = '__all__'
        extra_kwargs = {'contacts': {'required': False}}


class ContactSerializer(serializers.ModelSerializer):
    contact_list = ContactListSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Contact
        fields = '__all__'
        extra_kwargs = {'contact_list': {'required': False}}
