from django.urls import path
from . import views

app_name='Inventory'
urlpatterns = [
 path('', views.index, name='index'),
 path('<int:Name_id>/',views.detail,name='detail'),
 path('<int:Name_id>/results/',views.results,name='results'),
 path('<int:Laptop_id>/',views.display_laptop,name='display_laptop')



 ]
