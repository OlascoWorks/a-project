from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import current_user, login_required
from . import update_site, db
from .models import Orders

views = Blueprint('views', __name__)

def get_track():
    for n in range(9):
        id = f'{id}{n}'
        
    ex_id = Orders.query.filter_by(tracking_id=id).first()  
    while ex_id:
        for n in range(9):
            id = f'{id}{n}'
        ex_id = Orders.query.filter_by(tracking_id=id).first()
        
    return id

@views.route('/', methods=['GET', 'POST'])
def home():
    user = current_user
    update_site(user)
        
    if request.method == 'POST':
        if user.is_authenticated:
            pck_name = request.form.get('pck-name')
            pck_address = request.form.get('pck-address')
            pck_number = request.form.get('pck-number')
            rcp_name = request.form.get('rcp-name')
            rcp_address = request.form.get('rcp-address')
            rcp_number = request.form.get('-rcp-number')
            method = request.form.get('select')
            item_no = request.form.get('item_no')
            weight = request.form.get('weight')
            description = request.form.get('description')
            extra = request.form.get('radio')
            
            if len(pck_number) < 11 or len(rcp_number) < 11:
                flash('Please put in valid numbers', 'error')
            elif len(pck_address) < 15 or len(rcp_number) < 15:
                flash('Please put in valid addresses', 'error')
            else:
                new_order = Orders(status='placed', tracking_id=get_track(), pck_name=pck_name, pck_address=pck_address, pck_number=pck_number, rcp_name=rcp_name, rcp_address=rcp_address, rcp_number=rcp_number, method=method, item_no=item_no, weight=weight, extra=extra, description=description)
                db.session.add(new_order)
                db.session.commit()
                flash("Your order has been placed successfully, you will be contacted shortly", 'success')
        else:
            flash('Please create an account or login to an existing account to be able to order', category='error')
            return redirect('signup/fop')
    
    return render_template('home.html', user=current_user)

@views.route('/about')
def about():
    user = current_user
    update_site(user)
        
    return render_template('about.html', user=current_user)

@views.route('/services')
def services():
    user = current_user
    update_site(user)
        
    return render_template('services.html', user=current_user)

@views.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    user = current_user
    update_site(user)
    
    if request.method == 'POST':
        if user.is_authenticated:
            pck_name = request.form.get('pck-name')
            pck_address = request.form.get('pck-address')
            pck_number = request.form.get('pck-number')
            rcp_name = request.form.get('rcp-name')
            rcp_address = request.form.get('rcp-address')
            rcp_number = request.form.get('-rcp-number')
            method = request.form.get('select')
            item_no = request.form.get('item_no')
            weight = request.form.get('weight')
            description = request.form.get('description')
            extra = request.form.get('radio')
            
            if len(pck_number) < 11 or len(rcp_number) < 11:
                flash('Please put in valid numbers', 'error')
            elif len(pck_address) < 15 or len(rcp_number) < 15:
                flash('Please put in valid addresses', 'error')
            else:
                new_order = Orders(status='placed', tracking_id=get_track(), pck_name=pck_name, pck_address=pck_address, pck_number=pck_number, rcp_name=rcp_name, rcp_address=rcp_address, rcp_number=rcp_number, method=method, item_no=item_no, weight=weight, extra=extra, description=description)
                db.session.add(new_order)
                db.session.commit()
                flash("Your order has been placed successfully, you will be contacted shortly", 'success')
        else:
            flash('Please create an account or login to an existing account to be able to order', category='error')
            return redirect('signup/fop')
        
    return render_template('order.html', user=current_user)