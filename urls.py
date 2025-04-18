from django.urls import path
from . import views

urlpatterns = [
    # ... existing urls ...
    path('auth/firebase/', views.firebase_auth, name='firebase_auth'),
] 