from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Genre(models.Model):
    category = models.CharField(max_length=20)

    def __unicode__(self):
        return self.categorya

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    language = models.CharField(max_length=100)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    genre = models.ForeignKey(Genre)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title
