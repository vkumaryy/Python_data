from django.db import models

# Create your models here.

from django.db import models

class PdfDetail(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    filename = models.CharField(max_length=255)
    tax_invoice_no = models.CharField(max_length=255, blank=True)  # Allow empty tax invoice number
    status = models.CharField(max_length=50, choices=[
        ('PROCESSING', 'Processing'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ], default='PROCESSING')  # Default status

    def __str__(self):
        return self.filename

    def save_from_json(self, data):
        self.filename = data.get('filename', '')  # Handle potential missing filename
        self.tax_invoice_no = data.get('tax_invoice_no', '')
        self.save()

