from django.http import HttpResponse


def index(request):
    return HttpResponse('<div>Hello dwg!</div>')
