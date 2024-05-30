from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dog_index, name='dog-index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog-detail'),

    path('dogs/create/', views.DogCreate.as_view(), name='dog-create'),

    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog-update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog-delete'),

    path('dogs/<int:dog_id>/add-walk/', views.add_walk, name='add-walk'),
    path('snacks/create/', views.SnackCreate.as_view(), name='snack-create'),

    path('snacks/<int:pk>/', views.SnackDetail.as_view(), name='snack-detail'),
    path('snacks/', views.SnackList.as_view(), name='snack-index'),
    path('snacks/<int:pk>/update/', views.SnackUpdate.as_view(), name='snack-update'),
    path('snacks/<int:pk>/delete/', views.SnackDelete.as_view(), name='snack-delete'),
]