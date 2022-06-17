from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='app_index'),
    path('home/', views.home, name='app_index'),

]
