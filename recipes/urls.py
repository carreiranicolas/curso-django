from recipes.views import home, about, contact
from django.urls import path

urlpatterns = [

    path('', home), #Página inicial
    path('sobre/', about), #Página de sobre 
    path('contato/', contact) #Página de contato

]