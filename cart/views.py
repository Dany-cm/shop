from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from cart.cart import Cart
from order.models import Order
from product.models import Products


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, "cart/partials/cart_menu.html")


def cart(request):
    return render(request, "cart/cart.html")

@login_required
def success(request):
    order = Order.objects.filter(user=request.user, paid=True)
    if order.exists:
        order = order.first()
        return render(request, 'cart/success.html', {'order': order})


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Products.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
            },
            'total_price': (quantity * product.price) / 100,
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_item.html', {'item': item })
    response['HX-Trigger'] = 'update-cart-menu'

    return response


@login_required
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    return render(request, "cart/checkout.html", {'pub_key': pub_key})


def hx_cart_menu(request):
    return render(request, "cart/partials/cart_menu.html")


def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')
