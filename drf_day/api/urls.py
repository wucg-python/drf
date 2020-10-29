from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from api import views
urlpatterns = [
    path('api/<id>/',views.UserAPIView.as_view()),
    path('api/',views.UserAPIView.as_view()),

]