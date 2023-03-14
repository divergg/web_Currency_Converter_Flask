import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange

class CurrencyEntryForm(FlaskForm):
    CHOICES = [
        ('GBP', 'GBP'),
        ('USD', 'USD'),
        ('RUB', 'RUB'),
        ('TRY', 'TRY'),
        ('GEL', 'GEL')
    ]

    choose_from_currency = wtforms.SelectField(choices=CHOICES, label='First currency')
    choose_to_currency = wtforms.SelectField(choices=CHOICES, label='Second currency')
    from_currency = wtforms.DecimalField(validators=[DataRequired(), NumberRange(min=1, max=1000000)], label="Enter value")
    submit = wtforms.SubmitField('Calculate')



