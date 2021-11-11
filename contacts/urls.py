from django.urls import path, re_path, include
from . import views
from contacts.views import ContactViewSet, ContactListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/contacts', ContactViewSet, basename='contact')
router.register('api/contact-lists', ContactListViewSet, basename='contact-list')
# router.urls

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api/contact-lists/name/(?P<name>.+)/$', views.ContactListDetail.as_view(), name='contact-list-search'),
]
