from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    # No need form model
    model = Review
    fields = '__all__'
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['message'] = 'User has been created...'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        query =  super().get_queryset()
        return query  # rating__gt=4


class SingleReviewView(DetailView):
    template_name = 'reviews/detail.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        loaded_review = self.object
        favourite_id = self.request.session.get("fav_review")

        context['is_favourite'] = favourite_id == str(loaded_review.id)
        return context


class FavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["fav_review"] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
