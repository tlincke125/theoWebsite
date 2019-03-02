from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import *

urlTemplates = {'aboutTemplate':'about.html', 'projectTemplate':'projects.html', 'aboutTheo':'aboutTheo.html', 'postsTemplate':'posts.html', 'contactTemplate':'contact.html'}

mathPosts = Post.objects.filter(category = "math")
codePosts = Post.objects.filter(category = "electronics")
electricPosts = Post.objects.filter(category = "coding")

contextPosts = {"mathPosts" : mathPosts, "codePosts" : codePosts, "electricPosts":electricPosts}

featuredPost = Post.objects.filter(featured = True)
recentPost1 = Post.objects.filter(recent1 = True)
recentPost2 = Post.objects.filter(recent2 = True)
postList = Post.objects.order_by('-date')

contextMain = {"postList" : postList, "featured" : featuredPost, "recent1" : recentPost1, "recent2" : recentPost2}
print(recentPost1)
# Create your views here.
def renderHome(render):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(contextMain))

def renderAbout(render):
    template = loader.get_template(urlTemplates['aboutTemplate'])
    return HttpResponse(template.render())

def renderProjects(render):
    template = loader.get_template(urlTemplates['projectTemplate'])
    return HttpResponse(template.render())

def renderAboutMe(render):
    template = loader.get_template(urlTemplates['aboutTheo'])
    return HttpResponse(template.render())

def renderPosts(render):
    template = loader.get_template(urlTemplates['postsTemplate'])
    return HttpResponse(template.render(context))

def renderContact(render):
    template = loader.get_template(urlTemplates['contactTemplate'])
    return HttpResponse(template.render())

def renderBlogPost(render, category, idVar):
    template = loader.get_template(f'posts/{category}/{idVar}.html')
    return HttpResponse(template.render())

def renderPostMain(render, category):
    template = loader.get_template(f'posts/{category}.html')
    return HttpResponse(template.render(contextPosts))


def renderCubePage(render):
    template = loader.get_template('posts/coding/cube.html')
    return HttpResponse(template.render())
