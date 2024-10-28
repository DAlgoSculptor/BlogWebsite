from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify
# from django.contrib import messages

@login_required(login_url='Login')
def dashboard(request):
    category_counts = Category.objects.count()
    blogs_counts = Blogs.objects.count()

    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {'form': form}
    return render(request, 'dashboard/add_categories.html', context)

def edit_categories(request, pk):
    # Use a different variable name to avoid confusion with the model class
    category_instance = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_instance)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category_instance)

    context = {
        'form': form,
        'category': category_instance  # Use a clear context variable
    }
    return render(request, 'dashboard/edit_categories.html', context)


def delete_categories(request, pk):

    category_instance = get_object_or_404(Category, pk=pk)
    category_instance.delete()

    return redirect('categories')




def posts(request):
    posts = Blogs.objects.all()
    context ={
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)


def add_posts(request):
    if request.method=="POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.author=request.user
            post.save()
            title =form.cleaned_data['title']
            post.slug= slugify(title)
            post.save()
            # form.save()
            print("Success")
            return redirect('posts')
        
        else:
            print(form.errors)    
    form = BlogPostForm()

    context ={
        'form': form
    }
    return render(request, 'dashboard/add_posts.html', context)


def edit_posts(request, pk):
    post_instance = get_object_or_404(Blogs, pk=pk)  # Get the blog post instance

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post_instance)  # Bind the form to the post instance
        if form.is_valid():
            form.save()  # Save the changes
            return redirect('posts')  # Redirect to the posts list
    else:
        form = BlogPostForm(instance=post_instance)  # Load the current data into the form

    context = {
        'form': form,
        'post': post_instance  # Pass the current post to the template
    }
    return render(request, 'dashboard/edit_posts.html', context)


def delete_posts(request, pk):
    post_instance = get_object_or_404(Blogs, pk=pk)  # Get the blog post instance
    post_instance.delete()  # Delete the post
    return redirect('posts')  # Redirect to the posts list    
