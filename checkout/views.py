from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I8Q8YI4qPXLqrm5idWUN4jQFFgyGrcC3Dl7TmHkhPOx5iZUmfeK6SK74tTnsAv98va8X4ErNTB0xKBeLPg4DbYB00opqCG87k',
    }

    return render(request, template, context)
