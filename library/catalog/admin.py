from django.contrib import admin
from .models import Author, Genre, Language, Book,BookInstance

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)