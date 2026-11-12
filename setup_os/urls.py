from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chamados.urls')),  # Aponta para as rotas do app chamados
]