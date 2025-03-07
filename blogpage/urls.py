from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('contact', views.contact_view, name="contact"),
    path('success', views.success_view, name="success"),
    path('about', views.about, name="about"),
    path('more', views.more, name="more"),
    path('index/blog-1', views.blog1, name="blog-1"),
    path('index/blog-2', views.blog2, name="blog-2"),
    path('index/blog-3', views.blog3, name="blog-3"),
    path('index/blog-4', views.blog4, name="blog-4"),
    path('index/blog-5', views.blog5, name="blog-5"),
    path('index/blog-6', views.blog6, name="blog-6"),
    path('index/blog-7', views.blog7, name="blog-7"),
    # path('carousel', views.carousel_page, name="carousel"),
]
