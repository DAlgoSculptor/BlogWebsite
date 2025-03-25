from django.contrib import admin
from django.urls import path, include
from . import views  # Importing views from the current directory
from django.conf import settings  # For accessing MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static  # To serve media files during development
from blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel route
    path('/', views.home, name="home"),  # Home page route
    path('category/', include('blogs.urls')),  # Include URLs from the 'blogs' app
    path('blogs/<slug:slug>/', BlogsView.blogs , name='blogs'),
    path('search/' , BlogsView.search, name='search'),
    path('register/', views.register , name='register'),
    path('login/', views.login , name='Login'),
    path('logout/' , views.logout , name='logout'),
    path('dashboard/', include('dashboards.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # Serving media files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
