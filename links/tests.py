from django.test import TestCase
from django.urls import reverse

from links.models import Link
from links.views import get_tiny_link, open_tiny_link


def create_tiny_link(orig_link):
    link = Link.objects.create(
        orig_link=orig_link,
        tiny_link=get_tiny_link(orig_link=orig_link)
    )
    link.save()
    return link


class LinkModelTests(TestCase):
    # get_tiny_link() returns tiny link for original link
    def test_get_tiny_link(self):
        link = create_tiny_link(
            "https://django.fun/tutorials/usovershenstvovannoe-otobrazhenie-form-bootstrap-4-s-pomoshyu-django-crispy-forms/")
        self.assertIs(link.tiny_link, get_tiny_link(
            "https://django.fun/tutorials/usovershenstvovannoe-otobrazhenie-form-bootstrap-4-s-pomoshyu-django-crispy-forms/"))

    def test_increase_follow_quantity(self):
        # follow_quantity of new link after increase returns 1
        link = create_tiny_link(
            "https://django.fun/tutorials/usovershenstvovannoe-otobrazhenie-form-bootstrap-4-s-pomoshyu-django-crispy-forms/")
        link.follow_quantity += 1
        link.save()
        self.assertIs(link.follow_quantity, 1)


class LinkIndexViewTests(TestCase):

    def test_created_link(self):
        link = create_tiny_link(
            "https://django.fun/")
        url = reverse('links:index')
        response = self.client.get(url)
        self.assertContains(response, link.tiny_link)

    def test_deleted_link(self):
        link = create_tiny_link(
            "https://django.fun/")
        link.delete()
        url = reverse('links:index')
        response = self.client.get(url)
        self.assertNotContains(response, link.orig_link)
