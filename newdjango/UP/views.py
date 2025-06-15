from django.shortcuts import render, HttpResponse
from django.core.handlers.wsgi import WSGIHandler
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Collection, Category, Clothes
from .forms import ClothesForm
# Create your views here.
def first_page(request: WSGIHandler):
    return render(request, 'first_page.html')

def second_page(request: WSGIHandler):
    return render(request, 'second_page.html')

class ClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'

class ClothesDetailView(DetailView):
    model = Clothes
    template_name = 'clothes/clothes_detail.html'
    context_object_name = 'clothes'

class ClothesCreateView(CreateView):
    model = Clothes
    form_class = ClothesForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list')

class ClothesUpdateView(UpdateView):
    model = Clothes
    form_class = ClothesForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('clothes_list')

class ClothesDeleteView(DeleteView):
    model = Clothes
    template_name = 'clothes/clothes_delete.html'
    success_url = reverse_lazy('clothes_list')