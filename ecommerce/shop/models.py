from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the customer")
    email = models.EmailField(unique=True, help_text="The email of the customer")

    def _str_(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,
        related_name="orders", 
        help_text="The customer who placed this order"
    )
    order_date = models.DateTimeField(auto_now_add=True, help_text="The date and time when the order was placed")
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="The total amount for the order"
    )

    def _str_(self):
        return f"Order #{self.id} by {self.customer.name}"