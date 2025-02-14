from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Replace with a User model if available
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking for {self.listing.title} by {self.user}'


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Replace with a User model if available
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Ratings from 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.listing.title} by {self.user}'

#________________________________alx_travel_app_0x02___________________

class TransactionStatus(models.TextChoices):
    PENDING = 'Pending'
    SUCCESS = 'Success'
    FAILED = 'Failed'

class Transaction(models.Model):
    transaction_reference = models. CharField(max_length=100, unique=True)
    phone_number = models. CharField(max_length=15)
    email_address = models. EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models. CharField(
    max_length=10,
    choices=TransactionStatus. choices,
    default=TransactionStatus. PENDING
)

created_at = models.DateTimeField(auto_now_add=True)

def _str_(self):
    return f"Transaction {self.transaction_reference} - {self.status}"

class Meta:
    verbose_name = "Transaction"
    verbose_name_plural = "Transactions"