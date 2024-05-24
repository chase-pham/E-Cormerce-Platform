# shop/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.db.models import Count
from .models import Product, OrderItem

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'shop/profile.html', {'form': form})

# shop/views.py
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_detail.html', {'order': order})

def recommended_products(user):
    user_orders = OrderItem.objects.filter(order__user=user).values('product_id')
    recommended = Product.objects.filter(id__in=user_orders).annotate(order_count=Count('orderitem')).order_by('-order_count')[:5]
    return recommended
