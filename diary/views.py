from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        'title': 'Tensionary',
    }
    return render(request, 'diary/index.html', params)