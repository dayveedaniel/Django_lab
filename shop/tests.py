from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class HomePageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


# class UserFactory(factory.Factory):
#     class Meta:
#         model = CustomUser
#
#
# class UserTestCase(TestCase):
#     def setUp(self):
#         self.test_user = UserFactory.create(
#             passport='12345t',
#             username='test_user',
#             email='test_user@gmail.com',
#             first_name='test_first',
#             last_name='test_last',
#             type='staff')
#
#     def test_user_created(self):
#         self.assertEqual(self.test_user.passport, '12345t')
#         self.assertEqual(self.test_user.username, 'test_user')
#         self.assertEqual(self.test_user.email, 'test_user@gmail.com')
#         self.assertEqual(self.test_user.first_name, 'test_first')
#         self.assertEqual(self.test_user.last_name, 'test_last')
#         self.assertEqual(self.test_user.type, 'staff')
#         self.assertNotEqual(self.test_user.type, 'patient')
