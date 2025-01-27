from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Path to store uploaded images

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    categories = []  # List to store checkbox options
    selected_categories = []  # List to store selected categories
    image = FileField('Image')
    submit = SubmitField('Add to Marketplace')

# Add your desired categories to the list
categories_list = ['Electronics', 'Fashion', 'Books', 'Home & Garden', 'Others']
ItemForm.categories = categories_list

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ItemForm()
    if form.validate_on_submit():
        # Get selected categories
        for category in categories_list:
            if request.form.get(category):
                form.selected_categories.append(category)

        # Handle image upload
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.image.data.save(filepath)

        # Add item to marketplace (replace with your actual logic)
        # ...

        return redirect(url_for('success'))  # Redirect to success page

    return render_template('index.html', form=form, categories=categories_list)

@app.route('/success')
def success():
    return "Item added to marketplace successfully!"

if __name__ == '__main__':
    app.run(debug=True)