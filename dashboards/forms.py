from django import forms
from blogs.models import Category, Blogs

class CategoryForm(forms.ModelForm):

    class Meta:
        model=Category
        fields='__all__'



class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blogs

        fields='__all__'

    class Meta:
        model = Blogs
        exclude = ['created_at', 'updated_at']  # Example of fields to exclude
