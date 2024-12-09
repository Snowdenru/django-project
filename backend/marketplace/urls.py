from django.urls import path
from marketplace import views

app_name = "marketplace"

urlpatterns = [
    path("", views.product_list, name='product_list'),
    path("product/<int:pk>/edit", views.product_edit, name='product_edit'),
]
