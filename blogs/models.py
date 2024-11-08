from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50, unique=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural ='Categories'

    def __str__(self):
        return self.category_name    

STATUS_CHOICE=(
    ('draft','Draft'),
    ('published', "Published")
)

class Blogs(models.Model):

    title = models.CharField(max_length=100 , unique='True')
    slug = models.SlugField(unique=True , blank=True)
    Category = models.ForeignKey(Category , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=1000)
    blog_body = models.TextField(max_length=3000)
    status = models.CharField(max_length=100 , choices=STATUS_CHOICE , default='draft') 
    is_feacherd = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
     # TaggableManager for managing tags
    

    class Meta:
        verbose_name_plural ='blogs'

    def __str__(self):
       return self.title 
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)   
    comment = models.TextField(max_length=250)  # Lowercase 'comment'
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment  # Access the field with correct casing
