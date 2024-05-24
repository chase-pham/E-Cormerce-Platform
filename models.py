class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    # Other fields...

# shop/models.py
class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=10)  # 'percentage' or 'fixed'
    value = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

def apply_discount(request):
    if request.method == 'POST':
        code = request.POST['code']
        try:
            discount = Discount.objects.get(code=code, active=True)
            # Apply discount logic
        except Discount.DoesNotExist:
            # Handle invalid discount code
    return redirect('checkout')