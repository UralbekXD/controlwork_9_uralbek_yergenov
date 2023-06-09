from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_obj'] = self.request.user
        return context


class PhotoAddView(LoginRequiredMixin, CreateView):
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


class PhotoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/edit.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('index')

    def test_func(self):
        photo_id = self.kwargs.get('pk')
        photo = Photo.objects.get(pk=photo_id)

        curr_user = self.request.user
        targ_user = photo.author
        return (targ_user.username == curr_user.username) or curr_user.has_perm('gallery.change_photo')


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('index')

    def test_func(self):
        photo_id = self.kwargs.get('pk')
        photo = Photo.objects.get(pk=photo_id)

        curr_user = self.request.user
        targ_user = photo.author
        return (targ_user.username == curr_user.username) or curr_user.has_perm('gallery.delete_photo')


class AddFavouriteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_id = self.request.user.pk
        user = get_user_model().objects.get(pk=user_id)
        photo = Photo.objects.get(pk=kwargs.get('pk'))
        print(photo)

        photo.favourites.add(user)

        # Redirect to the same page
        return redirect('photo_detail', pk=kwargs.get('pk'))


class RemoveFavouriteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        account = get_user_model()
        user_id = self.request.user.pk
        user = account.objects.get(pk=user_id)
        photo = Photo.objects.get(pk=kwargs.get('pk'))
        print(photo)

        # user.favourites.remove(photo)
        photo.favourites.remove(user)

        # Redirect to the same page
        return redirect('photo_detail', pk=kwargs.get('pk'))
