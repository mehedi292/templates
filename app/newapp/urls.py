from django.urls import path
from .views import base_main,contact_main,about_main,index_main
urlpatterns =[
    path('', base_main),
    path('contact_main/', contact_main),
    path('about_main/', about_main),
    path('index_main/', index_main),
]
