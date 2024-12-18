from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .models import UploadedImage
from .forms import UploadImageForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadImageForm()
    images = UploadedImage.objects.all()
    return render(request, 'blog/upload_image.html', {'form': form, 'images': images})