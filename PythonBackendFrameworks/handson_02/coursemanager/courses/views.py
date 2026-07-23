from django.http import HttpResponse

def index(request):
    return HttpResponse("Course Management ORM Engine Active")
