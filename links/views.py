import hashlib
import uuid

import bcrypt as bcrypt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Link


class IndexView(generic.ListView):
    template_name = 'links/index.html'
    context_object_name = 'links_list'

    def get_queryset(self):
        return Link.objects.filter()


class CreateView(generic.CreateView):
    template_name = 'links/new.html'
    model = Link
    fields = ['orig_link']


def get_tiny_link(orig_link):
    tiny_link = bcrypt.hashpw(orig_link.encode('utf-8'), bcrypt.gensalt())
    return tiny_link.decode("utf-8")[30:40]


def create_tiny_link(request):
    orig_link = request.POST['orig_link']
    link = Link.objects.create(
        orig_link=orig_link,
        tiny_link=get_tiny_link(orig_link=orig_link)
    )
    link.save()
    return HttpResponseRedirect(reverse('links:index'))
