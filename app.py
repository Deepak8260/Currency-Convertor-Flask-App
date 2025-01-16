# Project: Currency Converter

from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Constants
JSON_FILE = 'data.json'

# Homepage Route
@app.route('/')
def index():
    try:
        # Read exchange rates from the local JSON file with UTF-8 encoding
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        rates = data.get("conversion_rates", {})
        ## print(rates) ##debugging code
        # Create a list of currency codes
        currencies = list(rates.keys())
        
        return render_template('index.html', currencies=currencies)
    except Exception as e:
        return f"Error reading data from JSON file: {e}", 500

# Conversion Route
@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        # Read exchange rates from the local JSON file with UTF-8 encoding
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        rates = data.get("conversion_rates", {})

        # Conversion logic
        if from_currency != 'USD':
            amount_in_usd = amount / rates[from_currency]['rate']
        else:
            amount_in_usd = amount

        converted_amount = amount_in_usd * rates[to_currency]['rate']

        return render_template('result.html', 
                               amount=amount,
                               from_currency=from_currency,
                               to_currency=to_currency,
                               converted_amount=round(converted_amount, 2))
    except Exception as e:
        return f"Error during conversion: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
