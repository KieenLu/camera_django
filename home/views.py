from django.shortcuts import render


# Create your views here.
def homePage (request):
    context ={}
    return render(request, "home/home.html", context)