from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
	list_display =('BooksName','EbooksAuthor','EbookReview','EbooksGenre')
# Register your models here.
admin.site.register(Books,BooksAdmin)