from django.urls import path
from home.views import Home, CarsView, Redirect, CarListView, CarDetailsView, CreateCarView, DeleteCarView, UpdateCarView
from home.views import MonthCarView


app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('car-list/', CarListView.as_view(), name='car-list'),
    path('two/', Redirect.as_view(), name='two'),

    # path('car/<int:pk>/', CarDetailsView.as_view(), name='car_details'),                            # using primary key
    # path('car/<slug:my_slug>/', CarDetailsView.as_view(), name='car_details'),                      # using slug
    path('car/<str:brand>/<str:model>/<int:year>/', CarDetailsView.as_view(), name='car_details'),    # using custome

    path('create-car/', CreateCarView.as_view(), name='create_car'),
    path('delete-car/<int:pk>', DeleteCarView.as_view(), name='delete_car'),
    path('update-car/<int:pk>', UpdateCarView.as_view(), name='update_car'),

    path('cars/<int:year>/<int:month>/', MonthCarView.as_view(), name='month_car')
]