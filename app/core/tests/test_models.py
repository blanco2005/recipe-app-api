from django.test import TestCase
from django.contrib.auth import get_user_model

INVALID_EMAIL = "invalidEmail"

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
            email=A_EMAIL_TO_NORMALIZE,
            password=A_PASSWORD
        )
        expected_email = A_EMAIL_TO_NORMALIZE.lower()
        self.assertEqual(user.email, expected_email)

    def test_email_is_not_valid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=INVALID_EMAIL,
                password=A_PASSWORD
            )

    def test_superuser_is_created(self):
        user = get_user_model().objects.create_superuser(
            email=A_NORMALIZED_EMAIL,
            password=A_PASSWORD
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
