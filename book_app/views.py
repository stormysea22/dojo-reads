from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from book_app.models import Review, Book, Author

@login_required
def review_list(request):
    context = {
        'reviews': Review.objects.order_by('-created_at')[:3],
        'books': Book.objects.all(),
    }
    return render(request, 'review_list.html', context)


@login_required
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    reviews = Review.objects.filter(user=user)
    total_reviews = reviews.count()
    context = {
        'reviews': reviews,
        'total_reviews' : total_reviews
    }

    return render(request, 'user.html', context)


@login_required
def create_book(request):
    if request.POST['author'] == "new":
        author = Author.objects.create(
            name=request.POST['new_author'],
        )
    else:
        author = Author.objects.get(id=request.POST['author'])

    book = Book.objects.create(
        title = request.POST['book_title'],
        rating = 0,
        user = request.user,
        author = author,
    )

    new_review = Review.objects.create(
        description= request.POST['review'],
        rating = int(request.POST['rating']),
        user=request.user,
        reviewed_book = book,
    )

    return redirect(f'/books/{book.id}')


@login_required
def add_book(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'add_book.html', context)


@login_required
def book_detail(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'authors': Author.objects.all(),
    }

    return render(request, 'book_detail.html', context)


@login_required
def create_review(request, book_id):
    Review.objects.create(
        description = request.POST['description'],
        rating = request.POST['rating'],
        user = request.user,
        reviewed_book = Book.objects.get(id=book_id)
    )
    return redirect(f'/books/{book_id}')


@login_required
class ReviewDelete(DeleteView):
    model = Review
    
    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'book_id' : self.kwargs['book_id']})

def login_redirect(request):
    return redirect('/accounts/login')
