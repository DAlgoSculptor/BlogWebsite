from django.shortcuts import render, HttpResponse, redirect
from .models import Blogs,Category,Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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

   # comment section
   comments = Comment.objects.filter(blog = single_post)
   comment_count =comments.count()
   if request.method=="POST":
      comment =Comment()
      comment.user = request.user
      comment.blog = single_post
      comment.comment = request.POST['comment']
      comment.save()
      
      return HttpResponseRedirect(request.path_info)


   
   # print(comments)
   context={
      'single_post': single_post,
      'comments':comments,
      'comment_count': comment_count          
   }
   return render(request , 'blogs.html' , context)


 

# search functionality
def search(request):
   keyword=request.GET.get('keyword')
   # comment
   
   # print(keyword)
   blogs= Blogs.objects.filter(Q (title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword), status='published')
   
   context={
      'blogs':blogs,
      'keyword': keyword
   }

   return render(request, 'search.html', context)