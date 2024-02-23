from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Brand, Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    brands = Brand.query.order_by(Brand.name).all()
    return render_template('index.html', brands = brands)

@bp.route('/product/<int:brandid>/')
def brandproducts(brandid):
    products = Product.query.filter(Product.brand_id == brandid)
    return render_template('brandproducts.html', products = products)

# Referred to as "Shopping Cart" to the user
@bp.route('/order', methods = ['POST', 'GET'])
def order():
    product_id = request.values.get('products_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # order will None if order_id wait too long
    else:
            # no order
            order = None

    # Create new order if needed
    if order is None:
        order = Order(status = False, firstname = '', lastname = '', email = '', phone = '', shippingaddress = '', billingaddress = '', totalcost = 0, date = datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order,id
        except:
            print('failed at creating a new order')
            order = None

    # Calculate the totalprice
    totalprice = 0
    if order is not None:
        for product in order.products:
            totalprice = totalprice + product.price

    # Check is it adding product
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the product to your shopping cart！'
            return redirect(url_for('main.order'))
        else:
            flash('product already in shopping cart')
            return redirect(url_for('main.order'))

    return render_template('order.html', order = order, totalprice = totalprice)

# Delete specific Shopping Cart product
@bp.route('/deleteorderitem', methods = ['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting product from order'
    return redirect(url_for('main.order'))

# Clear the Shopping Cart
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All products deleted')
    return redirect(url_for('main.index'))

@bp.route('/checkout', methods = ['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.shippingaddress = form.shippingaddress.data
            order.billingaddress = form.billingaddress.data
            order.phone = form.phone.data
            totalcost = 0
            for product in order.products:
                totalcost = totalcost + product.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you，We will send you the receipt soon...')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order！'
    return render_template('checkout.html', form = form)