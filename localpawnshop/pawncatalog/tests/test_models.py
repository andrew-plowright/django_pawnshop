from django.test import TestCase

from ..models import Customer

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')


    def test_first_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_first_and_last_name(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.first_name} {customer.last_name}'
        self.assertEqual(str(customer), expected_object_name)

    def test_get_absolute_url(self):
        customer = Customer.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(customer.get_absolute_url(), '/pawncatalog/customer/1')