import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from .models import classify_image


def clear_uploads_folder():
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
    if not os.path.exists(folder_path):
        return
    file_list = os.listdir(folder_path)
    if len(file_list) < 3:
        return
    file_paths = [os.path.join(folder_path, file) for file in file_list]
    file_paths.sort(key=os.path.getctime)
    for i in range(len(file_paths) - 3):
        os.remove(file_paths[i])


def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            fs = FileSystemStorage()
            filepath = os.path.join(settings.MEDIA_ROOT, "uploads", image.name)
            filename = fs.save(filepath, image)
            label = classify_image(filepath)

            # Get breed from the label
            breed = label.split("_")[1].capitalize() if "_" in label else label.capitalize()

            # Clear old files from the uploads folder
            clear_uploads_folder()

            # Pass the image back to the template
            return render(request, 'result.html', {'label': label, 'breed': breed, 'image_url': fs.url(filename)})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})