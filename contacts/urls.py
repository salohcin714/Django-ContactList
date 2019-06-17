from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_list'),
    path('new', views.ContactCreate.as_view(), name='contact_new'),
    path('edit/<int:pk>', views.ContactUpdate.as_view(), name='contact_edit'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
    path('view/<int:pk>', views.ContactDetail.as_view(), name='contact_view')
]
