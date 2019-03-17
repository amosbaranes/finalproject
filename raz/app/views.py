from django.shortcuts import render


def index(request):
    args = {'title': 'Home Page for App'}
    return render(request, 'app/app_home.html', args)
