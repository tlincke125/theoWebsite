from django.urls import path

from .views import *

urlpatterns = [
    path('posts/<str:category>/<str:idVar>/', renderBlogPost),
    path('posts/<str:category>/', renderPostMain),
    path('posts/coding/rubiksCube/cube/', renderCubePage, name='cubeMain'),

    path('about/', renderAbout, name='about'),
    path('projects/', renderProjects, name='projects'),
    path('theo/', renderAboutMe, name='aboutme'),
    path('posts/', renderPosts, name='posts'),
    path('contact/', renderContact, name='contact'),
    path('', renderHome, name='home'),
]
