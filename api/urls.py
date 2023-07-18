from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('list/', views.CarListView.as_view(), name='car_api_list'),
    path('<int:pk>/', views.SingleCarView.as_view(), name='car_api'),
    path('delete/<int:pk>', views.DeleteCarView.as_view(), name='car_api_delete'),
    path('create/', views.CreateCarView.as_view(), name='car_api_create'),
    path('update/<int:pk>', views.UpdateCarView.as_view()),

    path('generic', views.GenericHomeView.as_view()),
    path('generic/<int:pk>', views.GenericHomeView.as_view())
]