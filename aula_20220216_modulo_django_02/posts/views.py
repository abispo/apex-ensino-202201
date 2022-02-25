from django.views import generic

from .models import Post


class IndexView(generic.ListView):

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    model = Post
