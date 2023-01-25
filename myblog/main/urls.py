from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("post_detail/<int:pk>", views.DetailPageView.as_view(), name="detail"),
    path("add/", views.CreatePostView.as_view(), name="add"),
    path("update/<int:pk>", views.UpdatePostView.as_view(), name="update"),
    path("delete/<int:pk>", views.DeletePostView.as_view(), name="delete"),
]
