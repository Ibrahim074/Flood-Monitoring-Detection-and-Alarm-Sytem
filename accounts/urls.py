from django.urls import path

from .views import (HomeView, SignupPageView, UserView, 
                    AddLocationView, LocationView, LocationDeleteView, 
                    UserDeleteView, AddHomeView, HomeLocationView, HomeDeleteView)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("signup/", SignupPageView.as_view(), name="signup"),
    path("all_user/", UserView.as_view(), name="all_users"),
    path("all_user/<int:pk>/delete/", UserDeleteView.as_view(), name='delete_user'),

    path("add_location/", AddLocationView.as_view(), name="add_location"),
    path("all_location/", LocationView.as_view(), name='all_location'),
    path("all_location/<int:pk>/delete/", LocationDeleteView.as_view(), name='delete_location'),

    path("add_home/", AddHomeView.as_view(), name='add_home'),
    path("all_home/", HomeLocationView.as_view(), name='all_home'),
    path("all_home/<int:pk>/delete/", HomeDeleteView.as_view(), name='delete_home'),
]