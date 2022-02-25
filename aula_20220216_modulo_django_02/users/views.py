from django.shortcuts import render, get_object_or_404
from .models import User


def index(request):
    all_users = User.objects.all()
    context = {'all_users': all_users}

    return render(request, 'users/index.html', context)


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})
