from django.urls import path

from app import views

urlpatterns = [
    # path('user/',views.user),
    path('user/<id>/',views.UserView.as_view()),
    path('users/',views.UserApi.as_view()),

]
