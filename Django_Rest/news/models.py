from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=25)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=100)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

