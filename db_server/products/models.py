from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.currency} {self.amount}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=13, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name