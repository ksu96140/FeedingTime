from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.inventory import Inventory

#new inventory
@app.route('/shop_new')
def shop_new():
    data = {
        'user_id' : session['user_id']
    }
    session['inventory'] = Inventory.create(data)
    data.update({'id' : session['inventory']})
    print(data)
    session['gold'] = Inventory.gold(data)
    return render_template('shop.html', inventory=Inventory.view(data))

#updated inventory shop
@app.route('/shop_current')
def shop_current():
    data = {
        'user_id' : session['user_id'],
        'id' : session['inventory']
    }
    session['gold'] = Inventory.gold(data)
    return render_template('shop.html', inventory=Inventory.view(data))

#update inventory
@app.route('/purchase', methods=['POST'])
def purchase():
    data1 = {
        'user_id' : session['user_id'],
        'id' : session['inventory'],
        'carrot' : int(request.form['carrot']),
        'apple' : int(request.form['apple']),
        'rice' : int(request.form['rice']),
        'cheese' : int(request.form['cheese']),
        'fish' : int(request.form['fish']),
        'chicken' : int(request.form['chicken']),
        'blueberry' : int(request.form['blueberry']),
        'popcorn' : int(request.form['popcorn']),
        'gold' : int(session['gold'])
    }
    if not Inventory.purchase_valid(data1):
        return redirect('/shop_current')
    session['gold'] = session['gold'] - session['cartSum']
    session.pop('cartSum')
    data2 = {
        'user_id' : session['user_id'],
        'id' : session['inventory'],
        'gold' : session['gold']
    }
    Inventory.update(data1)
    Inventory.update_gold(data2)
    return redirect('/shop_current')
        

        
        