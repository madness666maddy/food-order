from django.shortcuts import render, redirect
from .models import Order
from menu.models import Food, Combo
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404


def place_order(request):
    # LOGIN CHECK
    if not request.session.get('user_id'):
        return redirect('/email-login/')  # change if your login URL differs

    #  If someone opens /order/ directly
    if request.method != "POST":
        return redirect('/')

    name = request.POST.get('customer_name')
    food_ids = request.POST.getlist('foods')
    combo_ids = request.POST.getlist('combos')

    total = 0
    foods = Food.objects.filter(id__in=food_ids)
    combos = Combo.objects.filter(id__in=combo_ids)

    for food in foods:
        total += food.price

    for combo in combos:
        total += combo.combo_price

    # CREATE ORDER
    order = Order.objects.create(
        customer_name=name,
        total_amount=total,
        order_status='Pending'
    )

    order.foods.set(foods)
    order.combos.set(combos)

    return render(request, 'orders/order_success.html', {
        'order': order
    })


def kitchen_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/kitchen_dashboard.html', {
        'orders': orders
    })


def update_status(request, order_id, status):
    order = Order.objects.get(id=order_id)
    order.order_status = status
    order.save()
    return redirect('/kitchen/')


client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_KEY_SECRET"))


def payment_page(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    razorpay_order = client.order.create({
        "amount": int(order.total_amount * 100), 
        "currency": "INR",
        "payment_capture": 1
    })

    order.payment_id = razorpay_order['id']
    order.save()

    return render(request, "orders/payment.html", {
        "order": order,
        "razorpay_key": "YOUR_KEY_ID",
        "razorpay_order_id": razorpay_order['id']
    })