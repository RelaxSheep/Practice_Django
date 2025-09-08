from django.db import models
from django.contrib.auth.models import User


# ========== Account & Address ==========
class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True, null=True)
    points = models.IntegerField(default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_detail = models.TextField()
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.address_detail}"


# ========== Category & Product ==========
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image_url = models.URLField()

    def __str__(self):
        return f"Image of {self.product.name}"


# ========== Voucher ==========
class DiscountType(models.TextChoices):
    PERCENT = 'P', 'Percent'
    AMOUNT = 'A', 'Amount'


class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=1, choices=DiscountType.choices, default=DiscountType.PERCENT)
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    begin_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.code


# ========== Order & OrderItem ==========
class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PAID = 'PAID', 'Paid'
    SHIPPED = 'SHIPPED', 'Shipped'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class PaymentMethod(models.TextChoices):
    COD = 'COD', 'Cash on Delivery'
    CARD = 'CARD', 'Credit/Debit Card'
    MOMO = 'MOMO', 'MoMo'
    BANK = 'BANK', 'Bank Transfer'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.SET_NULL, null=True, blank=True)
    establish_date = models.DateTimeField(auto_now_add=True)
    total_money = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices, default=PaymentMethod.COD)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
