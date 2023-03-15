from django.urls import path

from myblog.views import index, blog

urlpatterns = [
    path('', index, name='index'),
    path('<int:id_post>', blog, name='blog'),
]
