from flask import Flask, render_template, request, flash
import requests
from forms import CurrencyForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def get_conversion_rate(from_currency, to_currency, amount):
    try:
        access_key ='fa768efa1f20302e58c79937fe0af55a'
        response = requests.get(f"http://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&access_key={access_key}")
        data = response.json()
        return data['result']
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyForm()
    if form.validate_on_submit():
        from_currency = form.from_currency.data.upper()
        to_currency = form.to_currency.data.upper()
        amount = form.amount.data
        conversion_result = get_conversion_rate(from_currency, to_currency, amount)
        flash(f"The converted amount is {to_currency} {conversion_result:.2f}", 'success')
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                flash(f"Error in {fieldName}: {err}", 'error')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
