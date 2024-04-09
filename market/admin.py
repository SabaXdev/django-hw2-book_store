from django.contrib import admin
from market.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_count', 'category', 'author_name', 'price')
    search_fields = ('name', 'author_name')


admin.site.register(Book, BookAdmin)
