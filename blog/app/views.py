from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Post

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'app/index.html')

    def post(self, request):
        pass


class PostView(ListView):
    pass