# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from orders.forms import PaymentForm
from orders.models import Order


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def user_profile(request):
    current_user = request.user
    orders = Order.objects.filter(user=current_user)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        print(form)
    card_form = PaymentForm()
    context = {
        'user': current_user,
        'orders': orders,
        'form': card_form,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def complete_payment(request, order_id):
    print(request)
    print(request.POST)
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()
    message = f'''Your order has been successfully paid \n \n Order Details \n
            - Order ID: {order.id}
            - Date: {order.created}
            - Address: {order.address} {order.city}
            - Total: {order.get_total_cost()}

    Thank you for your Payment
          '''
    send_mail(f'Payment from AI options', message, None, [order.email])
    return redirect('profile')
