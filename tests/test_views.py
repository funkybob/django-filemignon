from django.test import TestCase 
from django.test.client import RequestFactory
from filemignon import views

class MyTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_delete(self):
        request = self.factory.delete('/thisfile')
        response = views.delete(request, 'thisfile')

        self.assertEqual(response.status_code, 204)

