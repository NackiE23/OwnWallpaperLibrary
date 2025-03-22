from django.core.paginator import Paginator
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Label


def index_view(request):
    labels = Label.objects.annotate(wallpaper_count=Count('wallpapers')).order_by('-wallpaper_count')
    wallpaper_list = None
    if request.GET.get('label'):
        try:
            wallpaper_list = get_wallpaper_list_by_label(request, request.GET['label']).content.decode('utf-8')
        except Http404:
            wallpaper_list = None

    context = {
        'title': 'Own Wallpaper Library',
        'labels': labels,
        'wallpaper_list': wallpaper_list,
    }
    return render(request, 'wallpaper_library/index.html', context)


def get_wallpaper_list_by_label(request, label_pk):
    label = get_object_or_404(Label, pk=label_pk)
    wallpapers = label.wallpapers.all()

    paginator = Paginator(wallpapers, 12)
    page = request.GET.get('page', '1')
    wallpapers = paginator.get_page(page)
    elided_page_range = paginator.get_elided_page_range(number=wallpapers.number, on_each_side=1, on_ends=2)

    context = {
        'title': label.name,
        'label': label,
        'wallpapers': wallpapers,

        # For the pagination
        'elided_page_range': elided_page_range,
        'get_wallpaper_list_by_label_url': reverse('get_wallpaper_list_by_label', kwargs={'label_pk': label_pk}),
    }
    response = render(request, 'wallpaper_library/parts/wallpaper_list.html', context)

    # Add HX-Replace-Url header to the response
    response['HX-Replace-Url'] = f"{reverse('index')}?label={label_pk}" + (f'&page={page}' if page != '1' else '')
    return response
