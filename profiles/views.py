from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile
from django.urls import reverse_lazy


# Create your views here.


class CreateProfile(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue') #change it to catalogue once the template is ready!!!


class EditProfile(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return Profile.objects.first()


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {'profile': profile}
    return render(request, 'profiles/delete-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, 'profiles/details-profile.html', context)

