from django import forms
import datetime
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Customer

class ChangeTransactionDate(forms.Form):

    trans_date = forms.DateField(label="Transaction date", help_text="When did this transaction occur?", required = True)

    # transaction_type = forms.ForeignKey('TransactionType', on_delete=models.RESTRICT)
    # customer = forms.ForeignKey('Customer', on_delete=models.RESTRICT)
    # item = forms.ForeignKey('Item', on_delete=models.CASCADE)

    def clean_trans_date(self):
        data = self.cleaned_data['trans_date']

        # Check if a date is not in the past.
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date from the future'))

        # Remember to always return the cleaned data.
        return data

class ChangeCustomerName(ModelForm):

    def clean_first_name(self):

        data = self.cleaned_data['first_name']

        if data == "Jerry":
            raise ValidationError(_('No customers can be named Jerry'))

        if len(data) < 2:
            raise ValidationError(_('First name must be at least two characters long'))

        return data

    # This is when field validation depends on each other
    def clean(self):

        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            self.add_error("first_name", "BAD!")
            self.add_error("last_name", "NOT GOOD!")
            raise ValidationError("First name and last name cannot be identical")

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']
        labels = {'first_name':_('First name'), 'last_name':_('Last name')}
        help_texts = {'first_name':_('Enter the customer\'s first name'), 'last_name':_('Enter the customer\'s last name')}
