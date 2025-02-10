from wtforms import RadioField, TextAreaField, DecimalField, IntegerField, validators, StringField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Optional
from flask_wtf import FlaskForm

class AddProductForm(FlaskForm):
    name = StringField("Product Name", [validators.DataRequired()])
    objectType = RadioField("Object Type", [validators.DataRequired()],
                            choices=[("C", "Clothes"), ("Pa", "Paper"), ("E", "Electronics"),
                                     ("Pl", "Plastics"), ("M", "Metals"), ("O", "Others")], default="")
    condition = RadioField("Condition", [validators.DataRequired()],
                           choices=[("G", "Good"), ("A", "Alright"), ("D", "Damaged")], default="A")
    weight = DecimalField("Weight(kg)", [validators.DataRequired()])
    quantity = IntegerField("Quantity of object(s)", [validators.DataRequired()])
    ppu = DecimalField("Price per unit (SGD)", [validators.DataRequired()])
    description = TextAreaField("Description (optional)", [validators.Optional()])
    image = FileField("Image of product", validators=[Optional(), FileAllowed(['jpg', 'png'], 'Images only!')])






















