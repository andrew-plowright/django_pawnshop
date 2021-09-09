import uuid

from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class ItemType(models.Model):

    name = models.CharField(max_length=100, help_text="What kind of item type?")

    def __str__(self):
        return self.name


class TransactionType(models.Model):

    name = models.CharField(max_length=100, help_text="What kind of transaction is it?")

    # Does this transaction bring the item into the store?
    in_store = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):

    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Unknown")
    country = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])


class Transaction(models.Model):

    transaction_type = models.ForeignKey('TransactionType', on_delete=models.RESTRICT)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    date = models.DateField(help_text="When did this transaction occur?")

    authorizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date']

        # Don't forget the trailing comma at the end here
        permissions = (("can_authorize", "Can authorize a transaction"),)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.date.__str__()} - {self.customer.first_name} {self.customer.last_name} - {self.transaction_type.name} - {self.item.name}'


class Item(models.Model):
    name = models.CharField(max_length=200, help_text="What is this item called?")
    type = models.ForeignKey(
        'ItemType',
        on_delete=models.RESTRICT,
        help_text="What type of item is this?")

    CONDITION = (
        ('n', 'New'),
        ('g', 'Gently used'),
        ('u', 'Used'),
        ('v', 'Very used')
    )

    condition = models.CharField(
        max_length=1,
        choices=CONDITION,
        blank=True,
        default='n',
        help_text='In what condition is this item?'
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('item-detail', args=[str(self.id)])

    def is_available(self):
        trans = self.transaction_set.all().order_by('-date')
        if(len(trans) == 0):
            return False
        else:
            last_trans = trans[0]
            return last_trans.transaction_type.in_store



