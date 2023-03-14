import random
import flask

from forms import CurrencyEntryForm
from api import get_rates
import os
from dotenv import load_dotenv

load_dotenv()

app = flask.Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def calculate():
    template_name = 'calculation.html'
    result = 0
    form = CurrencyEntryForm()
    if form.validate_on_submit():
        quantity = float(flask.request.form['from_currency'])
        cur_from = flask.request.form['choose_from_currency']
        cur_to = flask.request.form['choose_to_currency']
        result = get_rates(cur_from, cur_to, quantity)
    context = {
        'form': form,
        'result': result,
    }
    return flask.render_template(template_name, context=context)

