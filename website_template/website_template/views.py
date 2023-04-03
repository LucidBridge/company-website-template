from django.shortcuts import render
def home(request):
      return render(request, 'home.html')

def projects_home(request):
      return render(request, 'projects_home.html')

def about_me(request):
      return render(request, 'about_me.html')

def tutorials(request):
      return render(request, 'tutorials.html')