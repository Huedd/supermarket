from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("login/", views.login, name="login"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
]
