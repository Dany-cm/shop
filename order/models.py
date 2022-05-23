from django.db import models
from django.contrib.auth.models import User

from product.models import Products


class Order(models.Model):
    ORDERED = "ordered"
    SHIPPED = "shipped"
    STATUS_CHOICES = (
        (ORDERED, "Ordered"),
        (SHIPPED, "Shipped"),
    )

    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ('-created_at',)
    

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount / 100

        return 0


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Products, related_name="items", on_delete=models.CASCADE
    )
    price = models.IntegerField()
    quantity = models.IntegerField()


    def get_total_price(self):
        return self.price / 100
