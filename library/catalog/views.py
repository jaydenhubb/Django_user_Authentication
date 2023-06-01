from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author, BookInstance, Genre, Language
from django.views.generic import CreateView,DetailView

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    context={
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available
    }
    return render (request, 'catalog/index.html', context=context)


class BookCreate(CreateView): #CreateView automamtically looks for  'book_form.html in the templates
    model = Book
    fields = '__all__'

class BookDetail(DetailView):
    model = Book

