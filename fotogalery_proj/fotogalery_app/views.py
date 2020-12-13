from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Picture
from django.core import serializers
from django.http import JsonResponse


class HomeView(TemplateView):
    template_name = 'fotogalery_app/home.html'


class PictureView(View):
    def get(self, request):
        qs = Picture.objects.all()
        data = serializers.serialize('json', qs)
        return JsonResponse({'data': data}, safe=False)

