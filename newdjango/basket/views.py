from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from up1.models import Product, Order, PosOrder
from .forms import BasketAddProductForm, OrderForm
from .basket import Basket


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if len(basket) <= 0:
        return redirect('catalog')  # или куда ты хочешь
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = Order.objects.create(
        buyer_firstname=form.cleaned_data['buyer_firstname'],
        buyer_name=form.cleaned_data['buyer_name'],
        buyer_surname=form.cleaned_data['buyer_surname'],
        comment=form.cleaned_data['comment'],
        delivery_address=form.cleaned_data['delivery_address'],
        delivery_type=form.cleaned_data['delivery_type'],
        user=request.user 
    )

        order.price = basket.get_total_price()
        order.save()

        for item in basket:
            PosOrder.objects.create(
            product=item['product'],
            quantity=item['count'],  
            order=order
        )


        basket.clear()
        return redirect('basket_detail')

    return render(request, 'order/order_form.html', {'form_order': form})


@login_required
def open_order(request):
    context = {
        'form_order': OrderForm()
    }
    return render(request, 'order/order_form.html', context)
