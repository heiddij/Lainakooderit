from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

admin.site.site_url='/leffavuokraamo'

app_name = 'leffavuokraamo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('user/', views.user_page, name="user"),
    path('movies', views.movies, name="movies"),
    path('login_page/', views.login_page, name="login"),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('movies/<pk>/', views.MovieDetailsView.as_view(), name="moviedetails"),
    path('rent/<int:film_id>', views.rent_movie, name="rent_movie"),
    path('return/<int:rental_id>', views.return_movie, name="return_movie"),
    path('registeration/', views.registeration_page, name="registeration")
    
]
