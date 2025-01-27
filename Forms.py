from wtforms import RadioField, TextAreaField, DecimalField, IntegerField, validators
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm


class AddProductForm(FlaskForm):
    objectType = RadioField("Object Type", [validators.DataRequired()],
                            choices=[("C", "Clothes"), ("Pa", "Paper"), ("E", "Electronics"),
                                     ("Pl", "Plastics"), ("M", "Metals"), ("O", "Others")], default="")
    condition = RadioField("Condition", [validators.DataRequired()],
                           choices=[("G", "Good"), ("A", "Alright"), ("D", "Damaged")], default="A")
    collection = RadioField("Method for collection", [validators.DataRequired()],
                            choices=[("P", "Pick-up"), ("D", "Delivery")], default="P", )
    weight = DecimalField("Weight(kg)", [validators.DataRequired()])
    quantity = IntegerField("Quantity of object(s)", [validators.DataRequired()])
    ppu = DecimalField("Price per unit (SGD)", [validators.DataRequired()])
    description = TextAreaField("Description (optional)", [validators.Optional()])
    image = FileField("Image of product", [validators.DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
























