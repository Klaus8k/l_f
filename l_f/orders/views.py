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
        print(request.user.is_active)
        if request.user.is_active is False:
            form = OrderCreateForm()
        else:

            # if user is not None:
            #     if user.is_active:
            #         print('1111111111111111')
            form = OrderCreateForm(initial={'user_name': request.user,
                                            'phone_number': 'phone',
                                            'email': request.user.email,
                                            'address': 'adress',
                                            'telegram': 'telegram'})
    return render(request, 'orders/create.html', {'cart': cart,
                                                  'form': form})
