import pandas as pd

def total_sales(df):
    df['sales_total']= df.sale_amount * df.item_price
    return df

def day_and_month(df):
    df['month']= df.index.month_name()
    df['day_of_week']= df.index.day_of_week
    return df

def set_index(df):
    df= df.set_index('sale_date')
    return df