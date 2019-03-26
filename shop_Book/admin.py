from django.contrib import admin

from .models import Author, Book,shop

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(shop)

