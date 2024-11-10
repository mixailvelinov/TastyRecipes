from django.urls import path
from django.urls.conf import include

from recipes import views

urlpatterns = [
    path('catalogue/', views.Catalogue.as_view(), name='catalogue'),
    path('create/', views.CreateRecipe.as_view(), name='create-recipe'),
    path('<int:id>/', include([
        path('details/', views.DetailsRecipe.as_view(), name='details-recipe'),
        path('edit', views.EditRecipe.as_view(), name='edit-recipe'),
        path('delete/', views.delete_recipe, name='delete-recipe')
    ]))
]