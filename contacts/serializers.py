from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import Contact, ContactList


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Contact
        fields = ['id', 'phone_num', 'name', 'email_address', 'contact_list']
        extra_kwargs = {'contact_list': {'required': False}}

    def validate_phone_num(self, value):
        """
        Check the phone number format
        """
        validator = RegexValidator(regex=r'^\+?\d+$', message='Phone number cannot contains alphanumeric, numbers only.', code='invalid_phone_num')
        validator(value)
        if len(value) > 15:
            raise serializers.ValidationError(detail='Phone number is too short, must be less than 15 digits', code='invalid_phone_num')
        elif len(value) < 8:
            raise serializers.ValidationError(detail='Phone number is too short, must be greater than 8 digits', code='invalid_phone_num')
        return value


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = ContactList
        fields = ['id', 'name', 'contacts']
        extra_kwargs = {'contacts': {'required': False}}
