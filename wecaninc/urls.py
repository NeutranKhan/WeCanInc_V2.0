from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('activities', views.activities, name='activities'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('get_involve/', include('get_involve.urls')),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('policy/', views.policy, name='policy'),
    path('projects/', views.projects, name='projects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
