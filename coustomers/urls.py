from . import views
from django.urls import path

app_name = 'coustomers'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.createform, name='create'),
    path('<int:coustomer_id> ', views.display, name='display'),
    path('<int:coustomer_id>/pdf', views.GeneratePDF.as_view(), name='pdf'),
]