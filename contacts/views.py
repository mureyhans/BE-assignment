from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Contact, ContactList
from .serializers import ContactSerializer, ContactListSerializer


# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing Contacts.

    retrieve:
    Return the given Contact.

    create:
    Create a new Contact instance.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing Contact Lists.

    retrieve:
    Return the given Contact List.

    create:
    Create a new Contact List instance.

    partial_update:
    Update partially the given Contact List. Can be use to Add or Remove Contacts from a Contact List
    """
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer

    @action(detail=True)
    def get_contacts(self, request, pk):
        """
        get:
        Return a list of Contacts within given Contact List.
        """
        contacts = Contact.objects.filter(contact_list__id=pk)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class ContactListDetail(generics.ListAPIView):
    """
    get:
    Return list of Contact List based on name
    """
    serializer_class = ContactListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        name_to_search = name.replace("_", " ")
        return ContactList.objects.filter(name__icontains=name_to_search)

#
# @api_view(['GET'])
# def get_contacts_within_contact_list(request, pk):
#
#     if request.method == 'GET':
#         contacts = Contact.objects.filter(contact_list__id=pk)
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)
