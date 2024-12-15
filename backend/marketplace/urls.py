from django.urls import path
from marketplace import views

app_name = "marketplace"

urlpatterns = [
    path("", views.product_list, name='product_list'),
    path("product/<int:pk>/comment", views.product_comment, name='product_comment'),
    path("product/<int:pk>/edit", views.product_edit, name='product_edit'),
    path("product/<int:pk>/delete", views.product_delete, name='product_delete'),
    path("product/create", views.product_create, name='product_create'),
    
]
