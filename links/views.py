from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Link
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'links/index.html'
    context_object_name = 'links_list'

    def get_queryset(self):
        return Link.objects.filter()[:5]
