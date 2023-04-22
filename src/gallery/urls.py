from django.urls import path, include

from .views import PhotoDetailView, PhotoAddView, PhotoEditView, PhotoDeleteView
from .views import AddFavouriteView, RemoveFavouriteView

urlpatterns = [
    path('<int:pk>/detail/', PhotoDetailView.as_view(), name='photo_detail'),
    path('create/', PhotoAddView.as_view(), name='photo_create'),
    path('<int:pk>/edit/', PhotoEditView.as_view(), name='photo_edit'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),

    path('<int:pk>/favourite/add', AddFavouriteView.as_view(), name='favourite_add'),
    path('<int:pk>/favourite/remove', RemoveFavouriteView.as_view(), name='favourite_remove'),
]
