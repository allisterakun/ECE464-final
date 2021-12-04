from datetime import date
from flask import Flask, request, json, session, render_template, redirect, url_for, jsonify
from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os

import db_setup # has our script to setup the database
import queries as q # has our SQL queries since we dont want to clog up app.py

# import subprocess
# from subprocess import run # run script to load tables in
# import pymysql
# from pymysql import cursors

load_dotenv()
db_user = os.environ.get("MYSQL_DATABASE_USER")
db_password = os.environ.get("MYSQL_DATABASE_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE_DB")
db_host = os.environ.get("MYSQL_DATABASE_HOST")

app = Flask(__name__)
app.run()

app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host

mysql = MySQL(app)


@app.route("/")
@app.route("/login")
def login():
    # db_setup.setup()

    msg = ""

    _id = request.args.get("inputId")
    _username = request.args.get("inputUsername")
    _password = request.args.get("inputPassword")

    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM Login_ WHERE username ='" + _username + "' and password ='" + _password + "'")
    data = cursor.fetchone()

    if data:
        msg = "mlem"
        # session["id"] = _id
        # session["store_id"] = 
        return render_template("index.html", msg = msg)
    else:
        # return render_template("index.html", msg = msg)
        # return "test"
        return json.jsonify(data)


"""### Login route
given employee id, username, password
query for a match
if no match ask for info again / try again
if match get their role/position then get a session and move onto the correct page


    on the frontend
    employee should then be able to
        logout -> take them to login
        enter times -> take them to timesheets page
        inventory manager -> take them to inventory page
    manager
        employee time sheets -> take them to timesheets page

"""

"""
Determine the correct homepage
"""
@app.route("/home")
def homepage():
    
    _id = session["id"]
    cursor = mysql.connect().cursor()
    return jsonify({"position": q.getPosition(cursor, _id)})



"""### Logout route
redirect to login page
delete the session
"""
@app.route("/logout")
def logout():
    return redirect(url_for('login'))

"""### Add a timesheet card
we already have the employee id from class
given a work date, clock in time, clock out time, items sold

insert it
"""
@app.route("/newTimesheet", methods = ["POST"])
def createTimesheet():
    _id = session["id"]
    # parse from frontend POST request

    # insert into db
    cursor = mysql.connect().cursor() 
    q.add_timesheet(cursor, _id, work_date, clock_in_time, clock_out_time, items_sold)

    # return status code
    return 

"""
Review your own timesheet

"""
@app.route("/getTimesheet", methods = ["GET"])
def getTimesheet():
    _id = session["id"]
    
    # get all the timesheets for the current employee
    cursor = mysql.connect().cursor() 
    q.get_timesheet(cursor, _id)


    # return a table
    return


"""
Review all timesheets
"""
@app.route("/getAllTimesheet", methods = ["GET"])
def getAllTimesheets():

    _id = session["id"]
    cursor = mysql.connect().cursor()
    if q.getPosition(cursor, _id) == "Manager":
        
        # parse then return
        return q.get_all_timesheets(cursor, start_date, end_date)
        
    else:
        # error not a manager, status code
        pass



"""### Get amount to pay employee
we already have the store id

query for all the employee's pay for a given week from today and back
    for all employees who made a time card within this week
        get the clock out - clock in times (make sure they are in hours) and multiply by salary
    return type [employee id, total pay for given week]

"""
@app.route("/getAllPay", methods = ["GET"])
def getAllPay():
    pass
    # parse for a start and end date

    # call getPay()

    # return the total

def getPay(start_date, end_date):
    
    q.get_all_salary_info(cursor, start_date, end_date)
    # python logic to find the total costs

    # return total cost
    return 


"""Get Profit"""
@app.route("/getProfit", methods = ["GET"])
def getProfit():
    # parse
    

    # get all the prices sold within the start and end date - call getPay
        # return the difference, ie the profit and return it, jsonified
    q.getSoldAmountTotal(cursor, session["store_id"], start_date, end_date) - getPay(start_date, end_date)



"""Get Inventory"""
@app.route("/getInventory")
def getInventory():
    # parse item_type (string)

    # if no item_type (string)
        # get all inventory
        q.get_inventory_general(cursor, store_id)
        # return jsonify of table
    
    # else get specific inventory
        product_id = q.get_product_info(cursor, product_name)
        q.get_inventory_specific_product(cursor, store_id, product_id)
        # return jsonify of table
     

    
"""### Sell
given a product id, quantity, price to sell at

if quantity exceed the one in the inventory return an error since we dont have enough to sell

if we can sell then subtract the given quantity from the Inventory and add the given quantity to the purchases
    insert price sold at, quantity given, todays date into purchases

"""
@app.route("/sell")
def sell():

    # parse for quantity, product_name
    # _quantity = 
    _store_id = session["store_id"]
    _employee_id = session["id"]
    

    # lookup the product_id and sell_price based on the product_name, parse into two variables: product_id and selling price
    q.get_product_info(cursor, product_name)

    # lookup the quantity from inventory based on product_id and store_id
    q.get_quantity_specific_product(cursor, product_id, _store_id)

    # if the quantity > given quantity
        # sell
    if True:
        # add to the purchases table (current date: create variable)
        q.add_purchases(cursor, _employee_id, current_date, price_sold_at, product_id, quantity)
    
        # subtract from inventory ie update the quantity in inventory
        q.update_inventory(cursor, store_id, product_id, quantity - _quantity)

    # else return error


"""### Restock
given product_id and some quantity, todays date

insert
    look for the product id and update quantity by adding the current quantity with the given quantity

"""
@app.route("/restock")
def restock():
    # parse for product_name, quantity
    # _quantity 
    # lookup the product_id
    q.get_product_info(cursor, product_name)

    # check if product exists
    if q.product_exists(cursor, product_id):
        # update quantity
        quantity = q.get_quantity_specific_product(cursor, product_id, _store_id)
        q.update_inventory(cursor, store_id, product_id, quantity + _quantity)
    else:
        q.add_inventory(cursor, store_id, product_id, _quantity)





#if __name__ == "__main__":
#    app.run()