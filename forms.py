from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators
from wtforms.validators import ValidationError

# Custom validator to check for non-negative numbers
def non_negative(form, field):
    if field.data < 0:
        raise ValidationError('Amount must be non-negative')

class CurrencyForm(FlaskForm):
    from_currency = StringField(
        'From Currency', [validators.Length(min=3, max=3), validators.InputRequired()])
    to_currency = StringField('To Currency', [validators.Length(
        min=3, max=3), validators.InputRequired()])
    amount = FloatField('Amount', [validators.InputRequired()], render_kw={"type": "number", "step": "0.01"})
