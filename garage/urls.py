from django.contrib import admin
from django.urls import path, include # <--- Vérifiez que 'include' est bien là

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', include('atelier.urls')),
]