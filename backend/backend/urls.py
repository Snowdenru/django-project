"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


handler403 = 'system.views.handler403'
handler404 = 'system.views.handler404'
handler500 = 'system.views.handler500'

urlpatterns = [
    path("", views.index),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("my-book/", include("book.urls", namespace="book")),
    path("weather/", include("weather.urls", namespace="weather")),
    path("marketplace/", include("marketplace.urls", namespace="marketplace")),
    path("movie/", include("movie.urls", namespace="movie")),
    path("feedback/", include("feedback.urls", namespace="feedback")),
    path("todo/", include("todo.urls", namespace="todo")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
