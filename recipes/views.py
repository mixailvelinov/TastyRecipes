from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from profiles.models import Profile
from recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.models import Recipe
from django.urls import reverse_lazy


# Create your views here.


class CreateRecipe(CreateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = Profile.objects.first()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = Profile.objects.first()
        return context


class EditRecipe(UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    pk_url_kwarg = 'id'
    template_name = 'recipes/edit-recipe.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = Profile.objects.first()
        return context


def delete_recipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    form = DeleteRecipeForm(instance=recipe)
    profile = Profile.objects.first()

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue')

    context = {'recipe': recipe, 'form': form, 'profile': profile}
    return render(request, 'recipes/delete-recipe.html', context)

# class DeleteRecipe(DeleteView):
#     model = Recipe
#     form_class = DeleteRecipeForm
#     pk_url_kwarg = 'id'
#     template_name = 'recipes/delete-recipe.html'
#     success_url = reverse_lazy('catalogue')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = DeleteRecipeForm(instance=self.object)  # If you want to display form fields
#         context['profile'] = Profile.objects.first()
#         return context

class DetailsRecipe(DetailView):
    model = Recipe
    pk_url_kwarg = 'id'
    template_name = 'recipes/details-recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        context['ingredients_list'] = recipe.ingredients.split(', ')
        context['profile'] = Profile.objects.first()
        return context

class Catalogue(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['profile'] = Profile.objects.first()
        return context
