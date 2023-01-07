from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user
from .models import User
import random
from .models import Site, Orders

bck = Blueprint('bck', __name__)
sec_key = ''
for _ in range(10):
    k = random.randint(0,9)
    sec_key = f'{sec_key}{k}'

@bck.route('/admin/backend/12345/<int:key>', methods=['GET', 'POST'])
def backend(key):
    if key != 2478:
        return render_template('404.html'), 404
    
    if request.method == 'POST':
        user = current_user
        if user.is_authenticated:
            return render_template('404.html'), 404
        else:
            pin = request.form.get('pin')
            if pin == '24788742':
                return redirect(url_for('bck.admin'))
            else:
                return render_template('404.html'), 404
    
    return render_template('verify_admin.html')
    

@bck.route(f'/admin/backend/admin/{sec_key}')
def admin():
    visits = Site.query.filter_by(name='site').first().visits
    unique_visits = Site.query.filter_by(name='site').first().unique_visits
    orders = len(Orders.query.all())
    
    return render_template('admin.html', visits=visits, unique_visits=unique_visits, orders=orders)

@bck.route(f'/admin/backend/admin/{sec_key}/customers')
def customers():
    return render_template('customers.html', users=User.query.all(), enu_users=enumerate(User.query.all()), sub_users=User.query.filter_by(is_subscriber=True).all(), enu_sub_users=enumerate(User.query.filter_by(is_subscriber=True).all()))

@bck.route(f'/admin/backend/admin/{sec_key}/orders', methods=['POST', 'GET'])
def orders():
    if request.method == 'POST':
        filter_by = request.form.get('filter-by')
        if filter_by == 'all':
            orders = Orders.query.all()
        elif filter_by == 'way-pck':
            orders = Orders.query.filter_by(status='way to pickup')
        elif filter_by == 'pckd':
            orders = Orders.query.filter_by(status='picked up')
        elif filter_by == 'way-delv':
            orders = Orders.query.filter_by(status='way to delivery')
        elif filter_by == 'delvd':
            orders = Orders.query.filter_by(status='delivered')
        elif filter_by == 'comp':
            orders = Orders.query.filter_by(status='completed')
    
    return render_template('orders.html', orders=orders, enu_orders=enumerate(orders))