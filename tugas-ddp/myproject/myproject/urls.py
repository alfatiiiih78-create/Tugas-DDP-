from django.contrib import admin
from django.urls import path
# Ubah 'projects' menjadi 'websaya' sesuai nama aplikasi kamu
from websaya import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', views.index, name='index'),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('gallery/', views.gallery, name='gallery'),
]