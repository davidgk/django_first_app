from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>hello world</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')