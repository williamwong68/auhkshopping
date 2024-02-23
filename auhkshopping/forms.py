from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in Shopping Card
class CheckoutForm (FlaskForm):
    firstname = StringField("Please enter your first name", validators = [InputRequired()])
    lastname = StringField("Please enter your last name", validators = [InputRequired()])
    email = StringField("Please enter your email", validators = [InputRequired(), email()])
    shippingaddress = StringField("Please enter your shipping address", validators = [InputRequired()])
    phone = StringField("Please enter your phone number", validators = [InputRequired()])
    billingaddress = StringField("Please enter your billing address", validators=[InputRequired()])
    submit = SubmitField("Send to Adminstrator !")