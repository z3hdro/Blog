from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request, 'index.html')
