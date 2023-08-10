
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('my_app/', include('my_app.urls')),
]
