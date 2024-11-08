from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'created_at', 'updated_at']
    search_fields = ['category_name']  # Add search functionality for categories

admin.site.register(Category, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'Category', 'author', 
        'blog_image', 'status', 'is_feacherd', 
        'created_at', 'updated_at'
    )
    list_filter = ('status', 'author', 'Category', 'is_feacherd', 'created_at')  # Add filtering
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'Category__category_name', 'status')  
    list_editable = ('is_feacherd',)
    
    # # Display category name instead of the default Category object
    # def category_name(self, obj):
    #     return obj.Category.category_name
    # category_name.short_description = 'Category'

admin.site.register(Blogs, BlogAdmin)

admin.site.register(Comment)


