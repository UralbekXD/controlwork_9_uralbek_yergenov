from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Photo
from .forms import PhotoForm


class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/index.html'
    context_object_name = 'photos'
    ordering = '-created_at'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user_obj'] = self.request.user
        return context


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'gallery/detail.html'
    context_object_name = 'photo'


class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('index')

        return self.render_to_response(context={
            'form': form,
        })


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/edit.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('index')


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('index')
