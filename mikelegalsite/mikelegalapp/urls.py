from django.urls import path , include , re_path
from . import views
from django.urls import re_path as url


urlpatterns = [
    path('', views.movie_form,name='movie_insert'),
    path('<int:id>/', views.movie_form, name='movie_update'),
    path('list/', views.movie_list,name='movie_list'),
    path('delete/<int:id>/', views.movie_delete,name='movie_delete')

]