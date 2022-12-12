from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField

class AddCupcakeForm(FlaskForm):
    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    quantity = IntegerField("Quantity?")
    is_healthy = BooleanField("This is a Healthy Snack")
    
    category = RadioField("Category", choices = [('ic','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy/Sweets')])
    
