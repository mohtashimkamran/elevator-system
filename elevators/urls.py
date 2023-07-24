
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('list',views.ElevatorViewSet.as_view({'get':'list'})),
    path('create',views.ElevatorViewSet.as_view({'post':'create'}))
]
