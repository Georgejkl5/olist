import pandas as pd
import numpy as np
from math import sqrt

from src.data.get_data import Olist
from src.features.build_features import get_months

data = Olist.get_data()

def get_quantity():
    return data['order_items'].groupby('seller_id')[['order_id']].nunique().rename(columns ={'order_id': 'n_orders'})

def get_price_and_review():
    df = data['order_items'][['order_id', 'seller_id', 'price']].merge(
        data['order_reviews'],
        on ='order_id', how ='outer')[[
        'order_id', 'seller_id', 'price', 'review_score'
    ]].dropna()
    return df

def get_profits():
    """
    Returns a DataFrame with:
    'olist_revenue','olist_cost', 'olist_profit', 'months_on_list'
    """
    n_orders = get_quantity()
    df = get_price_and_review()
    months_on_olist = get_months()

    # comupte the review costs
    review_score_cost = {1:100, 2:50, 3:40, 4:0, 5:0}
    df['review_cost'] = df['review_score'].map(review_score_cost)

    # merge table with get_quantity and months_on_list
    df = df.groupby('seller_id').sum()
    df = df.merge(months_on_olist, on= 'seller_id', how= 'inner').merge(n_orders, on ='seller_id', how='inner')

    # compute the IT cost and the total cost
    df['it_cost'] = df['n_orders'].apply(lambda x: sqrt(x))
    factor = 500_000/df['it_cost'].sum()
    df['it_cost'] = df['it_cost'].apply(lambda x: x*factor)
    df['olist_cost']  = df['review_cost'] + df['it_cost']

    # compute the revenues
    df['olist_sale_revenue'] = df['price'] * 0.1
    df['olist_monthly_revenue'] = df['months_on_olist'] * 80
    df['olist_revenue'] = df['olist_sale_revenue'] + df['olist_monthly_revenue']

    # compute the profits
    df['olist_profit'] = df['olist_revenue'] - df['review_cost']
    df = df[['olist_revenue','olist_cost', 'olist_profit','months_on_olist']]

    return df
