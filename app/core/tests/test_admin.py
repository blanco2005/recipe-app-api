from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.admin_user = a_logged_super_user(self.client)
        self.user = a_user()
        self.another_user = another_user()

    def test_users_are_listed(self):
        response = self.client.get(list_users_url())

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.another_user.name)
        self.assertContains(response, self.another_user.email)


def a_logged_super_user(client):
    superuser = get_user_model().objects.create_superuser(email="email@email.com", password="password")
    client.force_login(superuser)
    return superuser


def a_user():
    return get_user_model().objects.create_user(
        email="email2@email.com",
        password="password2",
        name="name"
    )


def another_user():
    return get_user_model().objects.create_user(
        email="email3@email.com",
        password="password3",
        name="name3"
    )


def list_users_url():
    return reverse('admin:core_user_changelist')
