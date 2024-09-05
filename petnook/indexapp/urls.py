from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from.import views
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('movies/',views.movies,name='movies'),
    path('productdescription/<int:movie_id>/',views.productdescription,name='productdescription'),

    
    
    path('directors/',views.directors,name='directors'),
    path('director/<int:director_id>/movies/', views.director_movies, name='director_movies'),

    
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    
   

    

]