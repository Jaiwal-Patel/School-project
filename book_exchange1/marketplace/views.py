from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book, Grade
from .forms import BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    books = Book.objects.filter(available=True).order_by('-created_at')
    grades = Grade.objects.all()
    return render(request, "marketplace/index.html", {
        "books": books,
        "grades": grades
    })


@login_required
def create_listing(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.save()
            messages.success(request, "Book listed successfully!")
            return redirect("index")
    else:
        form = BookForm()

    return render(request, "marketplace/create.html", {
        "form": form
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "marketplace/detail.html", {
        "book": book
    })


@login_required
def my_listings(request):
    books = Book.objects.filter(seller=request.user)
    return render(request, "marketplace/my_listings.html", {
        "books": books
    })


@login_required
def mark_sold(request, book_id):
    book = get_object_or_404(Book, id=book_id, seller=request.user)
    book.available = False
    book.save()
    messages.info(request, "Marked as sold.")
    return redirect("my_listings")
def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "marketplace/login.html", {
                "message": "Invalid username or password."
            })

    return render(request, "marketplace/login.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "marketplace/register.html", {
                "message": "Passwords must match."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "marketplace/register.html", {
                "message": "Username already taken."
            })

        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "marketplace/register.html")