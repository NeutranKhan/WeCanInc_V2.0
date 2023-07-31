from django.urls import path
from . import views

# urlpatterns for blog posts

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/search', views.search, name='search'),
]
