from django.contrib import admin


from .models import FavoriteRecipe, Ingredient, RecipeIngredient, Recipe, ShoppingCart, Tag


# class IngredientsInLine(admin.TabularInline):
#     model = Recipe.ingredients.through


# # @admin.register(FavoriteRecipe)
# # class FavoriteAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'user', 'recipe']
# #     search_fields = ['user__username', 'user__email']

# @admin.register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'measurement_unit']
#     search_fields = ['name']


# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'author', 'favorites']
#     search_fields = ['name', 'author__username']
#     list_filter = ['tags']
#     inlines = (
#         IngredientsInLine,
#     )

#     def favorites(self, obj):
#         if FavoriteRecipe.objects.filter(recipe=obj).exists():
#             return FavoriteRecipe.objects.filter(recipe=obj).count()
#         return 0


# @admin.register(ShoppingCart)
# class ShoppingCartAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'recipe']
#     search_fields = ['user__username', 'user__email']


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'color', 'slug']
#     search_fields = ['name', 'slug']

# admin.site.register(FavoriteRecipe)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe']
    search_fields = ['user__username', 'user__email']

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'total_favorites')
    list_filter = ('name', 'author', 'tags')
    search_fields = ('name', 'author__username', 'tags__name')

    def total_favorites(self, obj):
        return obj.shoppingcart_set.count()
    total_favorites.short_description = 'Favorites Count'


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe']
    search_fields = ['user__username', 'user__email']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(RecipeIngredient)
admin.site.register(ShoppingCart)
admin.site.register(FavoriteRecipe)