import subprocess
from flask import Flask
# from subprocess import run # run script to load tables in
import pymysql
import os


app = Flask(__name__)

@app.route("/")
def index():
    print("Enter password:")
    password = input()
    os.system("mysql -u root -p"+ password +" < .\\b.sql ")

    # db = pymysql.connect("localhost", "user1", "PASSWORD", "ece464")

    os.system("mysql -u root -p" + password + " < .\\schema.sql")

    return "success"


"""### Login route
given employee id, username, password
query for a match
if no match ask for info again / try again
if match get their role/position then move onto the correct page

    on the frontend
    employee should then be able to
        logout -> take them to login
        enter times -> take them to timesheets page
        inventory manager -> take them to inventory page
    manager
        employee time sheets -> take them to timesheets page

"""
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
given a product id and a new date do a PUT request

"""



"""### Get amount to pay employee
we already have the store id

query for all the employee's pay for a given week from today and back
    for all employees who made a time card within this week
        get the clock out - clock in times (make sure they are in hours) and multiply by salary
    return type [employee id, total pay for given week]

"""

if __name__ == "__main__":
    app.run()