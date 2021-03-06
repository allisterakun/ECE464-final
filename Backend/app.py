from datetime import datetime, timedelta
from flask import Flask, request, json, session, render_template, redirect, url_for, jsonify
from flaskext.mysql import MySQL
from dotenv import load_dotenv
from flask_cors import CORS

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
db_secret = os.environ.get("SECRET")

app = Flask(__name__)
CORS(app)
app.run()
app.secret_key = db_secret

app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host

mysql = MySQL(app)


"""### Login route
given username, password
query for a match
if no match ask for info again / try again
if match then get a session to save employee_id and move onto the correct page


    on the frontend
    employee should then be able to
        logout -> take them to login
        enter times -> take them to timesheets page
        inventory manager -> take them to inventory page
    manager
        employee time sheets -> take them to timesheets page

"""
@app.route("/")
@app.route("/login", methods = ["POST"])
def login():
    # db_setup.setup()

    # msg = ""
    
    _username = request.json["inputUsername"]
    _password = request.json["inputPassword"]
    # _username = request.args.get("inputUsername")
    # _password = request.args.get("inputPassword")
    
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM Login_ WHERE username ='" + _username + "' and password ='" + _password + "'")
    data = cursor.fetchone()

    if data:
        # get employee_id, store_id
        # session["employee_id"] = data[0]
        employee_id = data[0]

        cursor = mysql.connect().cursor()
        temp = cursor.execute("SELECT store_id FROM Employees WHERE employee_id = '" + str(employee_id) + "'")
        store_id = cursor.fetchone()[0];

        return json.jsonify({"employee_id": employee_id , "store_id": store_id})
        # msg = "mlem"
        # return render_template("index.html", msg = msg)
    else:
        # return render_template("index.html", msg = msg)
        # return "test"
        return json.jsonify({"statusCode": "401", "msg":"Wrong Username or Password!"})


"""
Determine the correct homepage
"""
@app.route("/home", methods = ["GET"])
def homepage():
    
    _id =  request.args.get("employee_id")
    cursor = mysql.connect().cursor()
    return jsonify({"position": q.getPosition(cursor, _id)[0]})


"""### Logout route
redirect to login page
delete the session

@app.route("/logout")
def logout():
    session.pop("employee_id", None)
    session.pop("store_id", None)
    return json.jsonify({"statusCode": "200"})
    # return redirect(url_for('login'))
"""


"""### Add a timesheet card
we already have the employee id from class
given a work date, clock in time, clock out time, items sold

insert it
"""
@app.route("/newTimesheet", methods = ["POST"])
def createTimesheet():
    
    # parse from frontend POST request
    work_date = request.json["work_date"]
    clock_in_time = request.json["clock_in_time"]
    clock_out_time = request.json["clock_out_time"]
    items_sold = request.json["items_sold"]

    _id = request.json["employee_id"]
    # current_date = datetime.now().date()

    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(clock_out_time, FMT) - datetime.strptime(clock_in_time, FMT)
    
    if tdelta > timedelta(0) :
        # Valid interval
        # insert into db
        conn = mysql.connect()
        cursor = conn.cursor()
        q.add_timesheet(cursor, _id, work_date, clock_in_time, clock_out_time, items_sold)
        conn.commit()
        # insert into Timesheet values (1, 2021-12-08, 22:00, 22:00, 12); 

        # return status code
        return json.jsonify({"statusCode": "200"})
    else:
        return json.jsonify({"statusCode" : "401", "msg":"Wrong Time Interval"})


"""
Review your own timesheet

"""
@app.route("/getTimesheet", methods = ["GET"])
def getTimesheet():
    _id = request.args.get("employee_id");
    
    # get all the timesheets for the current employee
    cursor = mysql.connect().cursor() 
    data = q.get_timesheet(cursor, _id)
    
    # return a table
    return jsonify(data)


"""
Review all timesheets
"""
@app.route("/getAllTimesheet", methods = ["GET"])
def getAllTimesheets():

    _id = request.args.get("employee_id");
    store_id = request.args.get("store_id")

    cursor = mysql.connect().cursor()
    if q.getPosition(cursor, _id)[0] == "Manager":
        
        # parse then return
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        # start_date = request.json("start_date")
        # end_date = request.json("end_date")
        
        data = q.get_all_timesheets(cursor, store_id, start_date, end_date)

        return json.jsonify(data)
        
    else:
        # error not a manager, status code
        return json.jsonify({"statusCode": "405"})


"""### Get amount to pay employee
we already have the store id

query for all the employee's pay for a given week from today and back
    for all employees who made a time card within this week
        get the clock out - clock in times (make sure they are in hours) and multiply by salary
    return type [employee id, total pay for given week]

"""
@app.route("/getAllPay", methods = ["GET"])
def getAllPay():

    # parse for a start and end date
    # start_date = request.json("start_date")
    # end_date = request.json("end_date")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    store_id = request.args.get("store_id")

    # call getPay()
    total = getPay(store_id, start_date, end_date)

    # return the total
    return json.jsonify({"total": total})


def getPay(store_id, start_date, end_date):

    # find the total costs: what manager has to pay
    cursor = mysql.connect().cursor()
    salary_info = q.get_all_salary_info(cursor, store_id, start_date, end_date)
    
    # return total cost
    return sum(salary_info.values())


"""Get Profit"""
@app.route("/getProfit", methods = ["GET"])
def getProfit():
    # parse
    # start_date = request.json("start_date")
    # end_date = request.json("end_date")
    start_date = request.args.get("start_Date")
    end_date = request.args.get("end_Date")
    store_id = request.args.get("store_id")

    period = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days

    if period >= 0:
        # get all the prices sold within the start and end date - call getPay
            # return the difference, ie the profit and return it, jsonified
        cursor = mysql.connect().cursor()
        amount_sold = q.getSoldAmountTotal(cursor, store_id, start_date, end_date)
        profit = amount_sold - getPay(store_id, start_date, end_date)

        return json.jsonify({"profit": profit, "amount_sold": amount_sold})
    else:
        return json.jsonify({"statusCode" : "401", "msg": "Please Enter a Valid Period!"});


"""### Get Inventory
Given an item_type, theres only three (drink, fruit, meat)
    get all items in the current employee's store where the item_type matches

If there is no item_type get the entire store inventory

"""
@app.route("/getInventory", methods = ["GET"])
def getInventory():
    # parse item_type (string)
    # item_type = request.json("item_type")
    item_type = request.args.get("item_type")

    store_id =  request.args.get("store_id")

    # if no item_type (string)
    if item_type is None:
        # get all inventory
        cursor = mysql.connect().cursor()
        data = q.get_inventory_general(cursor, store_id)

        # return jsonify of table
        return json.jsonify(data)

    # else get specific inventory
    else:
        mappings = {"fruit": 1, "meat": 2, "drink": 3}
        cursor = mysql.connect().cursor()
        product_ids = q.get_product_info(cursor, store_id, mappings[item_type])
        data = q.get_inventory_specific_type_products(cursor, store_id, product_ids)
        return json.jsonify(data)
        # return jsonify of table


@app.route("/getProducts", methods = ["GET"])
def getProducts():
    
    store_id =  request.args.get("store_id")

    cursor = mysql.connect().cursor()
    data = q.get_all_product_name(cursor,store_id)

    return json.jsonify(data)
     
    
"""### Sell
given a product id, quantity, price to sell at

if quantity exceed the one in the inventory return an error since we dont have enough to sell

if we can sell then subtract the given quantity from the Inventory and add the given quantity to the purchases
    insert price sold at, quantity given, todays date into purchases

"""
@app.route("/sell", methods = ["POST"])
def sell():

    # parse for quantity, product_name
    # _quantity = request.json("quantity")
    # product_name = request.json("product_name")
    _quantity = int(request.json["quantity"])
    product_name = request.json["product_name"]

    _store_id =  request.json["store_id"]
    _employee_id =  request.json["employee_id"]
    
    current_date = datetime.now().date()

    # lookup the product_id and sell_price based on the product_name, parse into two variables: product_id and selling price
    cursor = mysql.connect().cursor()
    product_id, price_sold_at = q.get_specific_product_info(cursor, _store_id, product_name)
    
    # lookup the quantity from inventory based on product_id and store_id
    quantity = q.get_quantity_specific_product(cursor, product_id, _store_id)[0]

    # if product exists
    if product_id:
        # if the quantity > given quantity
            # sell
        if _quantity and quantity >= int(_quantity):
            # add to the purchases table (current date: create variable)
            conn = mysql.connect()
            cursor = conn.cursor()
            q.add_purchases(cursor, _employee_id, current_date, price_sold_at, product_id, _store_id, _quantity)
            conn.commit()
        
            # subtract from inventory ie update the quantity in inventory
            conn = mysql.connect()
            cursor = conn.cursor()
            q.update_inventory(cursor, _store_id, product_id, quantity - _quantity)
            conn.commit()
            return json.jsonify({"statusCode": "200"})
        else:
            return json.jsonify({"statusCode": "405", "msg":"Insufficient stock to sell!"})

    # else return error
    else:
        # error not enough supply to sell, status code
        return json.jsonify({"statusCode": "405"})


"""### Restock
given product_id and some quantity, todays date

insert
    look for the product id and update quantity by adding the current quantity with the given quantity

"""
@app.route("/restock", methods = ["POST"])
def restock():
    # parse for product_name, quantity
    # _quantity = request.json("quantity")
    # product_name = request.json("product_name")
    _quantity = int(request.json["quantity"])
    product_name = request.json["product_name"]
    
    _store_id = request.json["store_id"]

    # lookup the product_id
    if product_name:
        cursor = mysql.connect().cursor()
        product_id, _ = q.get_specific_product_info(cursor, _store_id, product_name)

        if product_id:
            # check if product exists
            if q.product_exists(cursor, product_id):
                # update quantity
                quantity = q.get_quantity_specific_product(cursor, product_id, _store_id)

                conn = mysql.connect()
                cursor = conn.cursor()
                q.update_inventory(cursor, _store_id, product_id, int(quantity[0]) + _quantity)
                conn.commit()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()
                q.add_inventory(cursor, _store_id, product_id, _quantity)
                conn.commit()

            return json.jsonify({"statusCode": "200"})

        else:
            # no such product
            return json.jsonify({"statusCode": "405"})
    else:
        # no product_name given
        return json.jsonify({"statusCode": "405"})

"""Get Purchases
Return all rows of purchases at a given store from most recent to least recent purchase
"""    
@app.route("/getPurchases", methods = ["GET"])
def getPurchases():

    store_id =  request.args.get("store_id")

    # store_id = session["store_id"]
    cursor = mysql.connect().cursor()
    data = q.get_all_purchases(cursor, store_id)
    for a in data:
            a["purchase_date"] = str(a["purchase_date"])
    return json.jsonify(data)




#if __name__ == "__main__":
#    app.run()