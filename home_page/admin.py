from django.contrib import admin
from .models import (
    Account, Address, Category, Product, ProductImage,
    Voucher, Order, OrderItem
)


# Register your models here.
# ========== Inline Models ==========
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


# ========== Main Models ==========
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "points", "phone_number")
    search_fields = ("user__username", "phone_number")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "address_detail", "is_default")
    search_fields = ("user__username", "address_detail")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name",)
    list_filter = ("category",)
    inlines = [ProductImageInline]


@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ("code", "discount", "discount_type", "begin_date", "end_date")
    list_filter = ("discount_type", "begin_date", "end_date")
    search_fields = ("code",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_money", "establish_date", "payment_method")
    list_filter = ("status", "payment_method", "establish_date")
    search_fields = ("user__username", "id")
    inlines = [OrderItemInline]


# OrderItem được quản lý qua inline trong OrderAdmin,
# nếu bạn muốn vẫn có thể register riêng:
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "unit_price", "subtotal")
    search_fields = ("order__id", "product__name")
