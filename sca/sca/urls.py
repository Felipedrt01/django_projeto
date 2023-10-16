from django.contrib import admin
from django.urls import path, include
from aplic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplic.urls')),
    # Adicione mais includes para outros aplicativos
]


