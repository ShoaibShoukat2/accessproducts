from django.db import models
from datetime import date

class AccessCode(models.Model):
    code = models.CharField(max_length=50, unique=True, help_text="Unique access code for customer.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class ProductDetails(models.Model):
    access_code = models.OneToOneField(AccessCode, on_delete=models.CASCADE, related_name='product_details')
    email = models.EmailField(help_text="Email associated with the product.")
    password = models.CharField(max_length=255, help_text="Password associated with the product.")
    activation_code = models.CharField(max_length=100, help_text="Activation code for the product.")
    product_link = models.URLField(help_text="URL link for the product.")
    description = models.TextField(help_text="Description of the product.")
    
    
    order_no = models.CharField(max_length=50, help_text="Order number associated with the product.", default="ORD000000")
    warranty_till = models.DateField(help_text="Date till the product warranty is valid.", default=date.today)
    
    def __str__(self):
        return f"Details for Access Code: {self.access_code.code}"





