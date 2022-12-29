import pandas as pd

def load_data():

    datafile_customers = "data/noahs-customers.csv"
    datafile_orders = "data/noahs-orders.csv"
    datafile_orders_items = "data/noahs-orders_items.csv"
    datafile_products = "data/noahs-products.csv"

    customers = pd.read_csv(datafile_customers, parse_dates=["birthdate"])
    orders = pd.read_csv(datafile_orders, parse_dates=["ordered", "shipped"])
    orders_items = pd.read_csv(datafile_orders_items)
    products = pd.read_csv(datafile_products)
    
    return customers, orders, orders_items, products