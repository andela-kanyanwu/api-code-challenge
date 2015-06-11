from django.contrib import admin
from product_api.models import Book, Author, Publisher, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)