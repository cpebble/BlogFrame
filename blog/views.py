from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from back import models

from datetime import datetime

#Variables
postCount = 3   # How many posts per page



# Create your views here.
def front(request):
    timeStamp = datetime.now()

    blogPost = models.Post.objects.filter(published__lt=timeStamp)[:postCount]
    return render(request, 'page.html', {'posts' : blogPost, 'page' : 0} )

def page(request, page):
    try:
        page = int(page)#page is passed as a string
    except Exception as e:
        return HttpResponse("Error occured: <br/> %s" % e)

    timeStamp = datetime.now()
    pFrom = page*postCount      #Slice from
    pTo   = (page+1)*postCount  #Slice to
    blogPosts = models.Post.objects.filter(published__lt=timeStamp)[pFrom:pTo]
    return render(request, 'page.html', {'posts' : blogPosts, 'page' : page})

def post(request, id):
    try:
        id = int(id)#page is passed as a string
        post = models.Post.objects.get(postId=id)
    except Exception as e:
        return HttpResponse("Post not found, or has not been created yet")
    # if post.published > datetime.now():
    #     return HttpResponse("Post not found, or has not been created yet")
    return render(request, 'post.html', {'post':post})

def author(request, authId):
    try:
        authId = int(authId)
        author = models.Author.objects.get(id=authId)
    except Exception as e:
        return HttpResponse("Author not found")
    return render(request, 'author.html', {'author' : author})
