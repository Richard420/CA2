from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order

def order_create(request):
    cart = Cart(request)
    if request.method =='POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.voucher:
                order.voucher = cart.voucher
                order.discount = cart.voucher.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            #clear the cart
            cart.clear()
            return render(request,
                            'orders/order/created.html',
                            {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                    'orders/order/create.html',
                    {'cart': cart, 'form':form})
@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                    'admin/orders/order/detail.html',
                    {'order': order})