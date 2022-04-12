from django.contrib import admin

from recipes.models import *


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Note)
admin.site.register(RecipeIngredient)

