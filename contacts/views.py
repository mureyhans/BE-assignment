from rest_framework import viewsets, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Contact, ContactList
from .serializers import ContactSerializer, ContactListSerializer


# Create your views here.
class ContactListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing contacts
    Implements `GET /api/contacts/` endpoint

    post:
    Create a new contact
    Implements `POST /api/contacts/` endpoint
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(generics.RetrieveDestroyAPIView):
    """
    get:
    Return the given Contact
    Implements `GET /api/contacts/{id}/` endpoint

    delete:
    Delete the given Contact
    Implements `DELETE /api/contacts/{id}/` endpoint
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @api_view(['GET'])
    def contact_list(self, pk):
        """
        get:
        Return a list of Contact List for given Contact.
        Implements `GET /api/contacts/{id}/contact-lists`
        """
        contact_lists = ContactList.objects.filter(contacts__id=pk)
        serializer = ContactListSerializer(contact_lists, many=True)
        return Response(serializer.data)


class ContactListViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing Contact Lists.
    Implements `GET /api/contact-lists/`

    retrieve:
    Return the given Contact List.
    Implements `GET /api/contact-lists/{id}`

    create:
    Create a new Contact List instance.
    Implements `POST /api/contact-lists/`

    partial_update:
    Update partially the given Contact List. Can be use to Add or Remove Contacts from a Contact List
    Implements `POST /api/contact-lists/{id}`
    """
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer

    @action(detail=True)
    def contacts(self, request, pk):
        """
        get:
        Return a list of Contacts within given Contact List.
        Implements `GET /api/contact-lists/{id}/contacts`
        """
        contacts = Contact.objects.filter(contact_list__id=pk)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class ContactListDetail(generics.ListAPIView):
    """
    get:
    Return list of Contact List based on name
    Implements `GET /api/contact-lists/name/{name}`
    """
    serializer_class = ContactListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        name_to_search = name.replace("_", " ")
        return ContactList.objects.filter(name__icontains=name_to_search)
