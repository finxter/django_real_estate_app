from django.urls import path
from .views import ( lists, retrieve, update,
                    create, delete )


urlpatterns = [
    path('', lists, name='home'),
    path('lists/<int:pk>/', retrieve, name='retrieve'),
    path('create-listing/', create, name='create'),
    path('listings/<int:pk>/edit/', update, name='update'),
    path('listings/<int:pk>/delete/', delete, name='delete'),
]
