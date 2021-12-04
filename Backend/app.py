from flask import Flask, request, json, session, render_template, redirect, url_for
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
        return render_template("index.html", msg = msg)
    else:
        # return render_template("index.html", msg = msg)
        # return "test"

        return json.dumps({'html':'<span>Enter the required fields</span>'})


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

"""### Restock
given product_id and some quantity, todays date

insert
    look for the product id and update quantity by adding the current quantity with the given quantity

"""

"""### Sell
given a product id, quantity, price to sell at

if quantity exceed the one in the inventory return an error since we dont have enough to sell

if we can sell then subtract the given quantity from the Inventory and add the given quantity to the purchases
    insert price sold at, quantity given, todays date into purchases

"""

"""### Update expiration date
given a product id and a new date do a PUT request, just update the value in the table
"""



"""### Get amount to pay employee
we already have the store id

query for all the employee's pay for a given week from today and back
    for all employees who made a time card within this week
        get the clock out - clock in times (make sure they are in hours) and multiply by salary
    return type [employee id, total pay for given week]

"""

#if __name__ == "__main__":
#    app.run()