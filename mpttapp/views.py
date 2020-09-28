from django.shortcuts import render
from mpttapp.models import Folder

# Create your views here.
def index_view(request):
    folder = Folder.objects.all()
    return render(request, "index.html", {'folder': folder})