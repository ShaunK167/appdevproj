from flask import Flask, render_template, request, redirect, url_for, flash
from Forms import AddProductForm
from werkzeug.utils import secure_filename
import os
import shelve, Product

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/want2sell', methods=['GET', 'POST'])
def sell_object():
    add_product_form = AddProductForm()
    if request.method == 'POST' and add_product_form.validate_on_submit():
        file = add_product_form.image.data
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            products_dict = {}
            try:
                db = shelve.open('marketplace.db', 'c')

                try:
                    products_dict = db['Products']
                except KeyError:
                    products_dict = {}

                product = Product.Product(
                    add_product_form.name.data,
                    add_product_form.objectType.data,
                    add_product_form.condition.data,
                    add_product_form.weight.data,
                    add_product_form.quantity.data,
                    add_product_form.ppu.data,
                    add_product_form.description.data,
                    filename
                )
                products_dict[product.get_product_id()] = product
                db['Products'] = products_dict
                db.close()
            except (EOFError, FileNotFoundError):
                try:
                    os.remove('marketplace.db')
                except FileNotFoundError:
                    pass
                db = shelve.open('marketplace.db', 'c')
                products_dict = {}
                product = Product.Product(
                    add_product_form.name.data,
                    add_product_form.objectType.data,
                    add_product_form.condition.data,
                    add_product_form.weight.data,
                    add_product_form.quantity.data,
                    add_product_form.ppu.data,
                    add_product_form.description.data,
                    filename
                )
                products_dict[product.get_product_id()] = product
                db['Products'] = products_dict
                db.close()

            return redirect(url_for('retrieve_products'))
        else:
            flash('Image upload failed. Please try again.')
            return redirect(url_for('sell_object'))
    return render_template('want2sell.html', form=add_product_form)


@app.route('/retrieveProducts')
def retrieve_products():
    products_dict = {}
    try:
        db = shelve.open('marketplace.db', 'r')
        try:
            products_dict = db['Products']
        except KeyError:
            products_dict = {}
        db.close()
    except (EOFError, FileNotFoundError):
        products_dict = {}

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)

    return render_template('retrieveProducts.html', count=len(products_list), products_list=products_list)


@app.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = AddProductForm()
    if request.method == 'POST' and update_product_form.validate_on_submit():
        products_dict = {}
        try:
            db = shelve.open('marketplace.db', 'w')
            products_dict = db['Products']

            product = products_dict.get(id)
            product.set_name(update_product_form.name.data)
            product.set_ObjectType(update_product_form.objectType.data)
            product.set_condition(update_product_form.condition.data)
            product.set_weight(update_product_form.weight.data)
            product.set_quantity(update_product_form.quantity.data)
            product.set_ppu(update_product_form.ppu.data)
            product.set_description(update_product_form.description.data)

            file = update_product_form.image.data
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                product.set_image(filename)

            db['Products'] = products_dict
            db.close()
        except (EOFError, FileNotFoundError):
            flash('An error occurred while updating the product. Please try again.')
            return redirect(url_for('update_product', id=id))

        return redirect(url_for('retrieve_products'))
    else:
        products_dict = {}
        try:
            db = shelve.open('marketplace.db', 'r')
            products_dict = db['Products']
            db.close()
        except (EOFError, FileNotFoundError):
            flash('An error occurred while retrieving the product details. Please try again.')
            return redirect(url_for('retrieve_products'))

        product = products_dict.get(id)
        update_product_form.name.data = product.get_name()
        update_product_form.objectType.data = product.get_objectType()
        update_product_form.condition.data = product.get_condition()
        update_product_form.weight.data = product.get_weight()
        update_product_form.quantity.data = product.get_quantity()
        update_product_form.ppu.data = product.get_ppu()
        update_product_form.description.data = product.get_description()

        return render_template('updateProduct.html', form=update_product_form)


@app.route('/deleteProduct/<int:id>', methods=['POST'])
def delete_product(id):
    products_dict = {}
    try:
        db = shelve.open('marketplace.db', 'w')
        products_dict = db['Products']

        products_dict.pop(id)

        db['Products'] = products_dict
        db.close()
    except (EOFError, FileNotFoundError):
        flash('An error occurred while deleting the product. Please try again.')

    return redirect(url_for('retrieve_products'))


if __name__ == '__main__':
    app.run()