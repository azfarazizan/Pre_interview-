# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 01:30:42 2023

@author: Azfar
"""

import csv

# Function to read data from a CSV file and return it as a list of dictionaries
def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data

# Read data from the CSV files
customers_data = read_csv_file('C:/Users/Azfar/OneDrive/Documents/Database/customers.csv')
invoices_data = read_csv_file('C:/Users/Azfar/OneDrive/Documents/Database/invoices.csv')
invoice_lines_data = read_csv_file('C:/Users/Azfar/OneDrive/Documents/Database/invoice_lines.csv')

# Create a dictionary to store customer names
customer_names = {int(customer['id']): customer['name'] for customer in customers_data}

# Perform the join and print the result
for invoice_line in invoice_lines_data:
    customer_id = int(invoice_line['invoice_id'])
    book_title = invoice_line['description']
    price = float(invoice_line['unit_price'])
    
    if customer_id in customer_names:
        customer_name = customer_names[customer_id]
        print(f"Customer Name: {customer_name}, Book Title: {book_title}, Price: {price}")
