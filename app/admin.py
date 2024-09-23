from django.contrib import admin
from .models import AccessCode, ProductDetails

class ProductDetailsInline(admin.StackedInline):
    model = ProductDetails
    can_delete = False
    verbose_name_plural = 'Product Details'

class AccessCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'email', 'activation_code',)
    search_fields = ('code', 'product_details__email', 'product_details__activation_code')

    inlines = (ProductDetailsInline,)

    def email(self, obj):
        return obj.product_details.email if hasattr(obj, 'product_details') else 'No details'

    def activation_code(self, obj):
        return obj.product_details.activation_code if hasattr(obj, 'product_details') else 'No details'

admin.site.register(AccessCode, AccessCodeAdmin)
