from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_listing, name="create"),
    path("book/<int:book_id>/", views.book_detail, name="detail"),
    path("my/", views.my_listings, name="my_listings"),
    path("sold/<int:book_id>/", views.mark_sold, name="mark_sold"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]