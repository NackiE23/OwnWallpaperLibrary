from django.shortcuts import render


def index_view(request):
    context = {
        'title': 'Own Wallpaper Library',
    }
    return render(request, 'wallpaper_library/index.html', context)
