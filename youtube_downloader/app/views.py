from django.shortcuts import render

# Create your views here.
def download_video(request):
    return render(request, 'index.html')