from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def first_page(request):
    object_list = Order.objects.all()
    ord1 = Order.objects.filter(order_name='Анна').values('order_name', 'id')
    ord2 = Order.objects.filter(order_name='Анна', id=9).exists()
    # ord1 = orders.values('order_name')
    form = OrderForm()
    return render(request, 'index.html', { 'object_list' : object_list,
                                           'form' : form,
                                           'ord1' : ord1,
                                           'ord2': ord2})

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    # Order.objects.create(order_name=name, order_phone=phone)
    return render(request, 'thanks.html', { 'name': name,
                                            'phone': phone})
