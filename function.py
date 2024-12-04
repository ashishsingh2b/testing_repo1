from django.http import response

def home(request):
    return response(request, 'home.html')