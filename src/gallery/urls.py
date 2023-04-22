from django.urls import path, include

from .views import PhotoDetailView, PhotoAddView, PhotoEditView, PhotoDeleteView

urlpatterns = [
    path('<int:pk>/detail/', PhotoDetailView.as_view(), name='photo_detail'),
    path('create/', PhotoAddView.as_view(), name='photo_create'),
    path('<int:pk>/edit/', PhotoEditView.as_view(), name='photo_edit'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]