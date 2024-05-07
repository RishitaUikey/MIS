from django.urls import path
from sadmin.views import astaff,acust,apro,aserv,delserv,delpro,upserv,uppro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
            path('astaff',astaff,name='astaff'),   
            path('acust',acust,name='acust') ,  
            path('apro',apro,name='apro'),
            path('aserv',aserv,name='aserv'),
            
            
            path('dels/<int:id>',delserv,name='delserv'),
            path('delp/<int:id>',delpro,name='delpro'),
            
            
            path('update/<int:id>',upserv,name='upserv'),
            path('updatep/<int:id>',uppro,name='uppro')
] 