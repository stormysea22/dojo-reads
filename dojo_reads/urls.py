from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('login_app.urls')),
]
