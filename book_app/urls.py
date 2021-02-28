from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_redirect, name="login_redirect"),
    path('books', views.ReviewList.as_view(), name="review_list"),
    # path('books/add', views.book_create, name="book_add"),
    # path('book/<int:book_id>', views.BookDetail.as_view(), name="book_detail")
]