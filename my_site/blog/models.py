from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=180)
    image = models.CharField(max_length=200) # models.ImageField(null=True)
    #image_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} - {self.author}"

