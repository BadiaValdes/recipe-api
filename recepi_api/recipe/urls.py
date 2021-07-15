from django.urls import path, re_path
from .view import category_api, recipe_api, userlike_api, difficulty_api, ingredient_api, producto_api, measure_api
from . import views

urlpatterns = [
    # root
    path('', views.api_root),

    # Category
    path('category/', category_api.CategoryList.as_view(), name="category"),
    re_path('category/(?P<pk>[0-9a-f]{10})/', category_api.CategoryDetails.as_view(), name="category_details"),

    # Difficulty
    path('difficulty/', difficulty_api.DifficultyList.as_view(), name="difficulty"),
    re_path('difficulty/(?P<pk>[0-9a-f]{10})/', difficulty_api.DifficultyDetail.as_view(), name="difficulty_details"),

    # Ingredient
    path('ingredient/', ingredient_api.IngredienttList.as_view(), name="ingredient"),
    re_path('ingredient/(?P<pk>[0-9a-f]{10})/', ingredient_api.IngredientDetail.as_view(), name="ingredient_details"),

    # Measurement
    path('measurement/', measure_api.MeasurementList.as_view(), name="measurement"),
    re_path('measurement/(?P<pk>[0-9a-f]{10})/', measure_api.MeasurementDetail.as_view(), name="measurement_details"),

    # Product
    path('product/', producto_api.ProductList.as_view(), name="product"),
    re_path('product/(?P<pk>[0-9a-f]{10})/', producto_api.ProductDetail.as_view(), name="product_details"),

    # Recipe
    path('recipe/', recipe_api.RecipeList.as_view(), name="recipe"),
    re_path('recipe/(?P<pk>[0-9a-f]{10})/', recipe_api.RecipeDetail.as_view(), name="recipe_details"),
    re_path('recipe/html/(?P<pk>[0-9a-f]{10})', recipe_api.RecipeHig.as_view(), name="recipe_html"),

    # User Like
    path('userLike/', userlike_api.UserLikeList.as_view(), name="userLike"),
    re_path('userLike/(?P<pk>[0-9a-f]{10})/', userlike_api.UserLikeDetail.as_view(), name="userLike_details"),
]
