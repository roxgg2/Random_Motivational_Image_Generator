from django.shortcuts import render

def home(request):
    image_url = ''
    if request.GET.get("btn"):
        image_url = 'https://zenquotes.io/api/image'
    return render(request, "home.html", {"image_url": image_url})
