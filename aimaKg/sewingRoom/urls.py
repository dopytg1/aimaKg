from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name='home_page'),
    path("category/<slug:cat_slug>/", ShowCategory.as_view(), name="category"),
    path("products", ShowAllProducts.as_view(), name="products")
]
