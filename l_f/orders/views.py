from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):

    cart = Cart(request)

    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], quantity=item['quantity'], price=item['price'])

            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/created.html', {'order': order})
    else:

        if request.user.is_active is False:
            form = OrderCreateForm()
        else:
            form = OrderCreateForm(initial={'user_name': request.user.profile.user,
                                            'phone_number': request.user.profile.phone_number,
                                            'email': request.user.email,
                                            'address': request.user.profile.adress,
                                            'telegram': request.user.profile.telegram}
                                   )
    return render(request, 'orders/create.html', {'cart': cart,
                                                  'form': form})
