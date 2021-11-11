from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from contacts.models import Contact, ContactList


# Create your tests here.
class ContactTests(APITestCase):
    contact_list_name = 'Contact List 1'

    def test_CRD_list_contact(self):
        """
        API Test for: Create, Retrieve, Delete and List Contact
        """
        # create
        url_list = reverse('contact-list')
        data = {
            'phone_num': '098576432',
            'name': 'Contact 1',
            'email_address': 'contact_1@email.com'
        }
        response = self.client.post(url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().phone_num, '098576432')

        # retrieve
        url_contact_detail = reverse('contact-detail', kwargs={'pk': 1})
        response = self.client.get(url_contact_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # list
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # delete
        response = self.client.delete(url_contact_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), 0)

    def test_CRD_list_contact_list(self):
        """
        API Test for: Create, Retrieve, Delete and List Contact
        """

        # create
        url_list = reverse('contact-list-list')
        data = {'name': self.contact_list_name}
        response = self.client.post(url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactList.objects.count(), 1)
        self.assertEqual(ContactList.objects.get().name, self.contact_list_name)

        # retrieve
        url_detail = reverse('contact-list-detail', kwargs={'pk': 1})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.contact_list_name)

        # list
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # delete
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ContactList.objects.count(), 0)

    def test_search_contact_list_by_name(self):
        # populate
        contact_list = ContactList(name=self.contact_list_name)
        contact_list.save()

        # search
        url_detail = reverse('contact-list-search', kwargs={'name': 'Contact'})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], self.contact_list_name)

    def test_list_contact_from_particular_contact_list(self):
        # populate Contact
        contact_a = Contact(phone_num='0123456', name='Contact A')
        contact_a.save()
        contact_b = Contact(phone_num='6543210', name='Contact B')
        contact_b.save()
        contacts = [contact_a, contact_b]

        # populate Contact List
        contact_list_1 = ContactList(name=self.contact_list_name)
        contact_list_1.save()
        contact_list_1.contacts.set(contacts)

        # list contacts
        url_detail = reverse('contact-list-get-contacts', kwargs={'pk': 1})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_add_remove_contact_from_contact_list(self):
        # populate Contact
        contact_a = Contact(phone_num='0123456', name='Contact A')
        contact_a.save()
        contact_b = Contact(phone_num='6543210', name='Contact B')
        contact_b.save()

        # populate Contact List
        contact_list_1 = ContactList(name=self.contact_list_name)
        contact_list_1.save()

        # add contacts to contact list
        data = {'contacts': [1, 2]}
        url_detail = reverse('contact-list-detail', kwargs={'pk': 1})
        response = self.client.patch(url_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["contacts"]), 2)

        # remove contact from contact list
        data = {'contacts': [2]}
        response = self.client.patch(url_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["contacts"]), 1)
        self.assertEqual(response.data["contacts"][0], 2)
