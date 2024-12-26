from django.core.management.base import BaseCommand
import pandas as pd
from orders.models import Product

class Command(BaseCommand):
    help = 'Import products from Excel file'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('C:\Users\Rahul\Downloads\product_data.xlsx')
        for _, row in df.iterrows():
            Product.objects.get_or_create(name=row['name'], amount=row['amount'])
        self.stdout.write(self.style.SUCCESS('Successfully imported products'))
