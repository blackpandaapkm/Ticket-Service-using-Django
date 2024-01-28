from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'front_page/main.html')

def topics_detail(request):
    return render(request, 'topics_detail.html')

def topics_listing(request):
    return render(request, 'topics_listing.html')

def contact(request):
    return render(request, 'contact.html')
