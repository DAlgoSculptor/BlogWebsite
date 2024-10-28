from django.shortcuts import render, HttpResponse, redirect
from .models import Blogs,Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

def posts_by_category(request, category_id):
    # Fetch posts with 'published' status and matching category ID
    posts = Blogs.objects.filter(status='published', Category=category_id)
    try:
     category =Category.objects.get(pk=category_id)
    except:
       return redirect('home')
    
    # category =get_object_or_404(Category , pk=category_id)
    # Pass the QuerySet to the template
    context = {
        'posts': posts,
        'category':category
    }
    return render(request, 'posts_by_category.html', context)


# blogs

def blogs(request, slug):
   
   single_post = get_object_or_404(Blogs,slug=slug, status='published')
   context={
      'single_post': single_post
   }
   return render(request , 'blogs.html' , context)




# search functionality
def search(request):
   keyword=request.GET.get('keyword')
   # print(keyword)
   blogs= Blogs.objects.filter(Q (title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword), status='published')
   
   context={
      'blogs':blogs,
      'keyword': keyword
   }

   return render(request, 'search.html', context)