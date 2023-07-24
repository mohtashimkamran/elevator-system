
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('list',views.ElevatorViewSet.as_view({'get':'list'})),
    path('create',views.ElevatorViewSet.as_view({'post':'create'})),
    path('get/<str:id>',views.ElevatorViewSet.as_view({'get':'retrieve'})),
    path('update',views.ElevatorViewSet.as_view({'post':'updateLiftCondition'})),
    path('navigate',views.ElevatorNavigation.as_view({'post':'navigate'}))
]
