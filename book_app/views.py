from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from book_app.models import Review, Book, Author

class ReviewList(ListView):
    model = Review, Book
    template_name = "review_list.html"

def login_redirect(request):
    return redirect('/accounts/login')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('planner_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)