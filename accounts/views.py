# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from orders.forms import PaymentForm
from orders.models import Order


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def user_profile(request):
    print('hereee')
    current_user = request.user
    orders = Order.objects.filter(user=current_user)

    card_form = PaymentForm()
    context = {
        'user': current_user,
        'orders': orders,
        'form': card_form,
    }
    return render(request, 'accounts/profile.html', context)
