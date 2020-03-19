from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .froms import *


class TweetCreate(CreateView):
    model = Tweet
    fields = ['text']


class TweetUpdate(UpdateView):
    model = Tweet
    fields = ['text']


class TweetDelete(DeleteView):
    model = Tweet
    success_url = reverse_lazy('core:home')


class TweetDetailView(DetailView):
    model = Tweet


class TweetListView(ListView):
    model = Tweet
    paginate_by = 10
