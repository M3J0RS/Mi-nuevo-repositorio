
from django.urls import path
from myapp import views
urlpatterns = [
    path('home/', views.index),
   path('servicios/', views.servicios),
   path('facturas/', views.facturas),

    # path('contacto/', views.contacto),
    # path('productos/', views.productos),
    # path('nosotros/', views.nosotros),
]