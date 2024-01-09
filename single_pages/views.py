from django.shortcuts import render

def main(request):
    return render(request, "single_pages/main.html")

def about_engineer(request):
    return render(request, "single_pages/about_engineer.html")

def login(request):
    return render(request, "single_pages/login.html")