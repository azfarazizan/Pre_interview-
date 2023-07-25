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

# Create a set to store the customer IDs with invoices
customers_with_invoices = set()

# Populate the set with customer IDs from invoices data
for invoice in invoices_data:
    customer_id = int(invoice['customer_id'])
    customers_with_invoices.add(customer_id)

# Find customers with no invoices
customers_without_invoices = [customer for customer in customers_data if int(customer['id']) not in customers_with_invoices]

# Print the result
for customer in customers_without_invoices:
    print(f"Customer ID: {customer['id']}, Name: {customer['name']}, Email: {customer['email']}, Tel: {customer['tel']}")
