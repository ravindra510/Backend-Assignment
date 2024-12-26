from celery import shared_task
from datetime import datetime
from .models import Product
import pandas as pd

# @shared_task
# def daily_task():
#     print("Daily task running at", datetime.now())


@shared_task
def import_products_from_excel(file_path):  
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        Product.objects.get_or_create(name=row['name'], amount=row['amount'])

