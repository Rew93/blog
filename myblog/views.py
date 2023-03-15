from django.shortcuts import render

from myblog.models import PostModel


# Create your views here.

def index(request):
    context = {'posts': PostModel.objects.order_by('-date')}
    return render(request, 'myblog/index.html', context)


def blog(request, id_post):
    context = {'post': PostModel.objects.get(id=id_post)}
    return render(request, 'myblog/blog.html', context)
