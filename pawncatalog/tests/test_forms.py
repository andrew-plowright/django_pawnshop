from django.test import TestCase
from django.utils import timezone

from ..forms import ChangeCustomerName

class ChangeCustomerNameTest(TestCase):
    def test_change_customer_name_form_identical_names(self):
        form = ChangeCustomerName(data={"first_name":"Same value", "last_name":"Same value"})

        self.assertEqual(form.errors['first_name'], ['BAD!'])
        self.assertEqual(form.errors['last_name'], ['NOT GOOD!'])
        self.assertEqual(form.errors['__all__'], ['First name and last name cannot be identical'])

