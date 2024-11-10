from django import forms

from recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']
        labels = {
            'title': 'Title:',
            'cuisine_type': 'Cuisine Type',
            'ingredients': 'Ingredients:',
            'instructions': 'Instructions:',
            'cooking_time': 'Cooking Time:',
            'image': 'Image URL:',
        }

        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'cooking_time': forms.NumberInput(attrs={'placeholder': 'Provide the cooking time in minutes.'}),
            'image': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
        }


class CreateRecipeForm(RecipeBaseForm):
    pass


class EditRecipeForm(RecipeBaseForm):
    pass


class DeleteRecipeForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True