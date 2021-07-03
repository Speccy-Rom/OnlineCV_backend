from django.shortcuts import render


def all_posts(request):
    context = {}
    return render(request, 'index.html', context)
