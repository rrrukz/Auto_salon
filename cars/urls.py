from  django.urls import path

from .views import home_page, car_detail, all_cars
urlpatterns=[
    path('',home_page,name='home'),
    path('cars/',all_cars, name='all_cars'),
    path('car/<int:car_id>/',car_detail, name='car_detail'),
]# new path for car detail