from django.urls import path, re_path, include
from . import views
from contacts.views import ContactListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/contact-lists', ContactListViewSet, basename='contact-list')

urlpatterns = [
    path('api/contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('api/contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),
    path('api/contacts/<int:pk>/contact-lists', views.ContactDetailView.contact_list, name='contact-contact-lists'),
    path('', include(router.urls)),
    re_path(r'^api/contact-lists/name/(?P<name>.+)/$', views.ContactListDetail.as_view(), name='contact-list-search'),
]
