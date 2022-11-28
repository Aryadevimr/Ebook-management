from django.db import models

# Create your models here.

class Books(models.Model):
	BooksId = models.AutoField(primary_key=True)
	BooksName = models.CharField(max_length=500)
	EbooksAuthor = models.CharField(max_length=500)
	EbooksGenre = models.CharField(max_length=500)
	EbookReview = models.IntegerField()
	Favourite = models.CharField(max_length=500)

