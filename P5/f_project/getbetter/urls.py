from django.urls import path
from .views import *

app_name='getbetter'

urlpatterns = [
    path('', home_page),
    path('feel/', feel , name = "feel" ),
    path('<int:id>/', result , name = "result"),
    path('post_info/' , post_info , name = "post_info"),
    path('post_info/post_info' , finish, name="finish")
]