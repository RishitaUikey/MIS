from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from staff.views import *

urlpatterns = [
    path('', staffhome, name='staffhome'), # for the staff home page 
    path('login/',login_user, name='login'), # url for login
    path('logout/',logout_user, name='logout'),
    path('register/',register_user, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
