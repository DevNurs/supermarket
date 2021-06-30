from django.db import models
from apps.products.models import Product
from django.contrib.auth import get_user_model
from apps.cart import choices

User = get_user_model()


class CartManager(models.Manager):
    def get_or_new(self, request):
        new = False
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id, status='open')
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated and not cart_obj.user:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = self.new(user=request.user)
            new = True
            request.session['cart_id'] = cart_obj.id
        return cart_id, new

    def new(self, user=None):
        user_obj = None
        if user and user.is_authenticated:
            user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='carts', on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='carts', blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=choices.CHOICES_CART, default=choices.OPEN)
    objects = CartManager()

    def __str__(self):
        return f"{self.id}"
