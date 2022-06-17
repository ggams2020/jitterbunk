#Code by Genna Gams based off of tutorial from django https://docs.djangoproject.com/en/2.2/intro/

from django.urls import path

from . import views

app_name = 'bunks'
urlpatterns = [
    #found as /bunks/
    path('', views.homepage, name = 'homepage'),
    #found as /bunks/allbunks/
    path('allbunks/', views.allbunks, name="allbunks"),
    #found as /bunks/bunk/
    path('bunk/', views.bunk, name='bunk'),
    #found as /bunks/[username]
    path('<un>/', views.personalbunks, name="personalbunks"),
    #post comes here
    path('bunk/submit/', views.submitbunk, name='submitbunk'),
]