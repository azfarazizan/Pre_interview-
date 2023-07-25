# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 01:40:14 2023

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

# Create a dictionary to store customer names and another to store the total books purchased for each customer
customer_names = {int(customer['id']): customer['name'] for customer in customers_data}
customer_books_count = {}

# Calculate the total number of books purchased for each customer
for invoice_line in invoice_lines_data:
    customer_id = int(invoice_line['invoice_id'])
    quantity = int(invoice_line['quantity'])
    
    if customer_id in customer_books_count:
        customer_books_count[customer_id] += quantity
    else:
        customer_books_count[customer_id] = quantity

# Find customers who purchased more than 5 books
customers_more_than_5_books = [(customer_id, customer_books_count[customer_id]) for customer_id in customer_books_count if customer_books_count[customer_id] > 5]

# Print the result
for customer_id, num_books_purchased in customers_more_than_5_books:
    customer_name = customer_names[customer_id]
    print(f"Customer ID: {customer_id}, Name: {customer_name}, Num Books Purchased: {num_books_purchased}")
