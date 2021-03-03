from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_redirect, name="login_redirect"),
    path('books/', views.review_list, name="review_list"),
    path('books/create', views.create_book, name="create_book"),
    path('books/add', views.add_book, name="book_add"),
    path('books/<int:book_id>', views.book_detail, name="book_detail"),
    path('books/<int:book_id>/review/create', views.create_review, name="create_review"),
    path('books/<int:book_id>/review/<int:pk>/delete', views.ReviewDelete.as_view(), name="delete_review"),
    path('user/<int:user_id>', views.user_detail, name="user"),

]