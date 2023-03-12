from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is home page. First step to Sber?</h1>')