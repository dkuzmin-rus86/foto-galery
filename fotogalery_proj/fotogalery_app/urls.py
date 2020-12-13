from django.urls import path
from .views import HomeView, PictureView

app_name = 'fotogalery_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/picture/', PictureView.as_view(), name='picture-list'),
]