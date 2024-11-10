from django.shortcuts import render

from profiles.models import Profile


# Create your views here.


def home(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, 'home-page.html', context)