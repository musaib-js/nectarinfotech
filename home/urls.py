from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name=  "index"),
    path('contact/', views.contact, name = "contact")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)