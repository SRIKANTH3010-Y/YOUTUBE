from django.shortcuts import render,redirect
from .models import Video
from .models import Item

def video(request):
    obj=Item.objects.all()
    return render(request,'video.html',{'obj':obj})


def display(request):
    videos = Video.objects.all()

    context ={
        'videos':videos,
    }

    return render(request,'videos.html',context)

def upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        videos = Video(title = title,video=video)
        videos.save()
        return redirect('videos')

    return render(request,'upload.html')