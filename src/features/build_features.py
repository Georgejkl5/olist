import pandas as pd
import numpy as np

from src.data.get_data import Olist

data = Olist.get_data()

## months on Olist
def get_months():
    """
    Returns a DataFrame with:
    'seller_id', 'date_first_sale', 'date_last_sale', 'months_on_olist'
    """
    orders_approved = data['orders'][['order_id','order_approved_at']].dropna()

    orders_sellers = orders_approved.merge(data['order_items'],
                                               on='order_id')[[
                                                   'order_id',
                                                   'seller_id',
                                                   'order_approved_at'
                                               ]].drop_duplicates()

    orders_sellers["order_approved_at"] = pd.to_datetime(orders_sellers["order_approved_at"])

    orders_sellers["first_sale_date"] = orders_sellers['order_approved_at']
    orders_sellers["last_sale_date"] = orders_sellers['order_approved_at']

    # Compute first and the last sale date.
    df = orders_sellers.groupby('seller_id').agg({
        "first_sale_date": min,
        "last_sale_date": max,
    })

    # Compute the months on list
    df['months_on_olist'] = round((df['last_sale_date']-df['first_sale_date']) / np.timedelta64(1, 'M'))

    return df
