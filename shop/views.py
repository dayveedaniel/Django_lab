from django.views.generic.list import ListView
from shop.models import Customer, Order, Ticker, Product


# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Ticker
    context_object_name = "list_of_tickers"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset


class ProductsListView(ListView):
    template_name = 'shop/tickers/details.html'
    model = Product
    context_object_name = "list_of_products"
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve related options for the current ticker
        context['tickers'] = self.object.options.all()
        return context


class CustomersListView(ListView):
    template_name = "customer.html"
    model = Customer
    context_object_name = "list_of_all_customers"


class OrdersListView(ListView):
    template_name = "orders.html"
    model = Order
    context_object_name = "list_of_all_orders"
