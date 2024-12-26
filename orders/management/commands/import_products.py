import pandas as pd
from django.core.management.base import BaseCommand
from orders.models import Product

class Command(BaseCommand):
    help = "Import products from an Excel file"

    def handle(self, *args, **kwargs):
        file_path = 'C:\Users\Rahul\Downloads\product_data.xlsx'
        data = pd.read_excel(file_path)

        for _, row in data.iterrows():
            Product.objects.get_or_create(name=row['name'], amount=row['amount'])
        self.stdout.write("Products imported successfully!")
