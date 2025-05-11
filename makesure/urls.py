from django.urls import path

from . import views

urlpatterns=[
    path('',views.website,name='website'),
    path('submit',views.submit,name='submit'),
    path('privacy',views.privacy,name='privacy'),
    path('terms',views.terms,name='terms'),
    path('',views.home,name='home'),
    path('booking_details',views.booking_details,name='booking_details')
]