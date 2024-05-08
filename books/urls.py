from django.urls import path, include
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="books-index"),
    path("create", views.createTemplate, name="books-createTemplate"),
    path("createBook", views.create, name="books-create"),
    path("<int:pk>/", views.show, name="book-detail"),
    path("edit/<int:pk>/", views.editTemplate, name="book-editTemplate"),
    path("<int:pk>/delete", views.destroy, name="book-destroy"),
]
