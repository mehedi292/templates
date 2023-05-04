from django.shortcuts import render

# Create your views here.

def base_main(request):
    return render(request,'base.html')

def index_main(request):
    return render(request,'index.html')

def contact_main(request):
    return render(request,'contact.html')

def about_main(request):
    return render(request,'about.html')

