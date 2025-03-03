import csv
import os

def load_exchange_rates(file_path):
    exchange_rates = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            currency, rate = row
            exchange_rates[currency] = float(rate)
    return exchange_rates

def convert_currency(amount, currency, exchange_rates):
    if currency in exchange_rates:
        return amount * exchange_rates[currency]
    else:
        return None

def main():
    file_path = 'currency.csv'
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return
    
    exchange_rates = load_exchange_rates(file_path)
    
    amount = float(input("How much dollar do you have? "))
    currency = input("What currency you want to have? ").upper()
    
    converted_amount = convert_currency(amount, currency, exchange_rates)
    
    if converted_amount is not None:
        print(f"\nDollar: {amount} USD")
        print(f"{currency}: {converted_amount}")
    else:
        print(f"Sorry, the currency '{currency}' is not available.")

if __name__ == "__main__":
    main()