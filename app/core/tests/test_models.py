from django.test import TestCase
from django.contrib.auth import get_user_model

A_PASSWORD = 'test'
A_NORMALIZED_EMAIL = 'prova@prova.com'
A_EMAIL_TO_NORMALIZE = "prova@PROVA.com"


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        user = get_user_model().objects.create_user(
            email=A_NORMALIZED_EMAIL,
            password=A_PASSWORD
        )

        self.assertEqual(user.email, A_NORMALIZED_EMAIL)
        self.assertTrue(user.check_password(A_PASSWORD))

    def test_email_is_normalized(self):
        user = get_user_model().objects.create_user(
            email=("%s" % A_EMAIL_TO_NORMALIZE),
            password=A_PASSWORD
        )
        expected_email = A_EMAIL_TO_NORMALIZE.lower()
        self.assertEqual(user.email, expected_email)
