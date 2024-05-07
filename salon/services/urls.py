from django.urls import path

from services.views import servi

urlpatterns = [
    path('',servi, name='service'),
]

