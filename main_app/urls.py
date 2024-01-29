from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('puppies/', views.puppies_index, name='index'),
  path('puppies/<int:puppy_id>/', views.puppies_detail, name='detail'),
]