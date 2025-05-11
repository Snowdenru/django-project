from django.urls import path
from api import views


urlpatterns = [
    path('v1/posts/', views.PostListView.as_view(), name=None),
    path('v1/posts/create/', views.PostCreateView.as_view(), name=None),
    path('v1/posts/<int:pk>/', views.PostDetailView.as_view(), name=None)
]