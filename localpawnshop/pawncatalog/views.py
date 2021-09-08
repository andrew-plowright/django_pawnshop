from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *

def index(request):

    # Number of visits to this view, as counted in the session variable.
    # Note that the 0 here is the default value if 'num_visits' is not present
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'count_transactions'   : Transaction.objects.all().count(),
        'count_items'          : Item.objects.all().count(),
        'count_itemtypes'      : ItemType.objects.all().count(),
        'count_activecustomers': Customer.objects.filter(active=True).count(),
        'num_visits'           : num_visits,
    }

    return render(request, 'index.html', context = context)

#@login_required
#@permission_required('catalog.can_authorize', raise_exception=True)
def change_transaction_date(request, pk):

    transaction = get_object_or_404(Transaction, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ChangeTransactionDate(request.POST)

        # Check if the form is valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            transaction.date = form.cleaned_data['trans_date']
            transaction.save()

            # redirect to a new URL:
            #return HttpResponseRedirect(reverse('index') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today()
        form = ChangeTransactionDate(initial={'trans_date': proposed_renewal_date})

    context = {
        'form': form,
        'transaction': transaction,
    }

    return render(request, 'transactions/transaction_change_date.html', context)


#@login_required
#@permission_required('catalog.can_authorize', raise_exception=True)
def change_customer_name(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ChangeCustomerName(request.POST)

        # Check if the form is valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            customer.first_name = form.cleaned_data['first_name']
            customer.last_name = form.cleaned_data['last_name']
            customer.save()

            # redirect to a new URL:
            #return HttpResponseRedirect(reverse('index') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = ChangeCustomerName(initial={'first_name': "", 'last_name': ""})

    context = {
        'form': form,
        'customer': customer,
    }

    return render(request, 'customers/customer_change_name.html', context)


# ListView is a generic type of view.
class ActiveCustomerListView(generic.ListView):

    model = Customer
    context_object_name = 'customers_list'
    template_name = 'customers/customer_active_list.html'
    queryset = Customer.objects.filter(active=True)


class CustomerDetailsView(generic.DetailView):

    model = Customer
    context_object_name = 'single_customer'
    template_name = 'customers/customer_single_detail.html'

    # Add extra custom context values
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Extra value passed from 'urls.py' (second argument
        # is if no value was defined)
        passed_extra_option = self.kwargs.get('test_context_value', 'No value was provided')

        context['andrew_custom_context_value'] = passed_extra_option
        return context


# ListView is a generic type of view.
class ItemsListView(generic.ListView):

    model = Item
    context_object_name = 'items_list'
    paginate_by = 4
    template_name = 'items/items_list.html'


class ItemDetailsView(generic.DetailView):

    model = Item
    context_object_name = 'single_item'
    template_name = 'items/item_single_detail.html'


class TransactionsAuthorizedByUser(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):

    model = Transaction
    context_object_name = 'authorized_transaction_list'
    template_name = 'transactions/transactions_authorized.html'
    paginate_by = 5

    permission_required = 'catalog.can_authorize'

    def get_queryset(self):
        # Get the current user
        authorizing_user = self.request.user
        return Transaction.objects.filter(authorizer=authorizing_user)


