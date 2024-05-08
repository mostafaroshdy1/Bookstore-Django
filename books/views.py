from django.shortcuts import render
from books.models import Book
from django.shortcuts import redirect

# Create your views here.


def index(request):
    context = {"books": Book.objects.all()}
    return render(request, "index.html", context)


def createTemplate(request):
    return render(request, "create.html")


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        rate = request.POST.get("rate")
        book = Book(title=title, description=description, rate=rate)
        book.save()
    return redirect("books:books-index")


def show(request, pk):
    book = Book.objects.get(pk=pk)
    context = {"book": book}
    return render(request, "show.html", context)


def editTemplate(request, pk):
    if request.method == "GET":
        book = Book.objects.get(pk=pk)
        context = {"book": book}
        return render(request, "edit.html", context)

    elif request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        rate = request.POST.get("rate")
        book = Book.objects.get(pk=pk)
        book.title = title
        book.description = description
        book.rate = rate
        book.save()
        return redirect("books:book-detail", pk=pk)


def destroy(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("books:books-index")
