from django.shortcuts import render
from apps.base.models import Name
# Create your views here.

def name_list(request):
    names = Name.objects.all()
    return render(request, "index.html", {"names": names})