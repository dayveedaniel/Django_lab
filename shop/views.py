from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from cart.form import CartAddProductForm
from shop.models import Customer, Order, Ticker


# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Ticker
    context_object_name = "list_of_tickers"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(full_name__icontains=search_query))

        return queryset


def ticker_details(request, slug):
    ticker = get_object_or_404(Ticker, slug=slug)
    options = ticker.tickers.all()
    cart_product_form = CartAddProductForm()
    context = {'ticker': ticker, 'options': options, 'cart_product_form': cart_product_form}
    return render(request, 'shop/tickers/details.html', context)


class CustomersListView(ListView):
    template_name = "customer.html"
    model = Customer
    context_object_name = "list_of_all_customers"


class OrdersListView(ListView):
    template_name = "orders.html"
    model = Order
    context_object_name = "list_of_all_orders"
