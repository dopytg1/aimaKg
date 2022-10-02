from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import *


class Home(ListView):
    model = Dress
    template_name = "sewingRoom/home.html"
    context_object_name = "dresses"

    def get_queryset(self):
        return Dress.objects.order_by("-id")[:4]


class ShowCategory(ListView):
    model = Dress
    template_name = "sewingRoom/product_cats.html"
    context_object_name = 'dresses'

    def get_queryset(self):
        return Dress.objects.filter(category_id__slug=self.kwargs['cat_slug'])


class ShowAllProducts(ListView):
    model = Dress
    template_name = "sewingRoom/all_products.html"
    context_object_name = "dresses"
    paginate_by = 12

