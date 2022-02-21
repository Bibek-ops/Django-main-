from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from app import views
from app.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('address')    
        self.assertEquals(resolve(url).func,address)

    def test_case_orders_url(self):
        url=reverse('orders')    
        self.assertEquals(resolve(url).func,orders)

    def test_case_showcart_url(self):
        url=reverse('showcart')    
        self.assertEquals(resolve(url).func,show_cart)


    def test_case_device_url(self):
        url=reverse('device')    
        self.assertEquals(resolve(url).func,mobile)


    def test_case_checkout_url(self):
        url=reverse('checkout')    
        self.assertEquals(resolve(url).func,checkout)

class Testviews(TestCase):
    def test_views_indbhex(self):
        client=Client()
        url=reverse('app:ProductDetailView')
        response=client.post(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"productdetail.html")


